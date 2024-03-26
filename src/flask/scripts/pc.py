from pathlib import Path
import subprocess
import json
import logging

logging.basicConfig(level=logging.DEBUG,  # logging level
                    filename=Path('bilicache.log'),
                    format='%(asctime)s-[%(filename)s-->line:%(lineno)d]-[%(levelname)s]%(message)s')

def validPathName(name:str):
    # 非法字符 '[:*?"<>|]'
    result = name.replace("[","")
    result = result.replace(":","")
    result = result.replace("*","")
    result = result.replace("?","")
    result = result.replace("\"","")
    result = result.replace("<","")
    result = result.replace(">","")
    result = result.replace("|","")
    result = result.replace("]","")
    # 最后不能以.结尾
    while result.endswith("."):
        result = result[:-1]
    # result = result.replace("！","")
    return result

def convert(val):
    FFMPEG_PATH = Path("resources", "app.asar.unpacked", "resources", "ffmpeg", "bin", "ffmpeg.exe").absolute()
    logging.warning('ffmpeg path: ' + str(FFMPEG_PATH))
    downloadDir = val['path']  # cache file root (should be tv.danmaku.bili/download/...)
    outputDir = val['output']  # output video file root
    CREATE_UP_DIR = val["isUp"] # 如果需要将同一个up的视频放在单独一个文件夹,则改为True
    # TRANS_DM = val['isDm']
    # REMOVE_ORI = val['isDel']  # True if would like to delete origin cache file

    BUFFER_SIZE = val["bufferSize"] # 分割大小，单位为MB
    
    logging.info("CREATE_UP_DIR: " + str(CREATE_UP_DIR))
    logging.info("BUFFER SIZE: " + str(BUFFER_SIZE))
    # logging.info("TRANS_DM: " + str(TRANS_DM))
    # logging.info("REMOVE_ORI: " + str(REMOVE_ORI))
        
    # collect failed
    failedVideos = []

    vRoot = Path(downloadDir)
    # outputDir = Path("E:/bcctest/tpc")  # output video file root
    logging.info("Current workspace: " + str(vRoot))

    try:
        for entry_path in list(filter(Path.is_dir, Path.iterdir(vRoot))):
            # entry_path = Path("E:/bcctest/140099078")

            input_files = []
            try:
                for entry_file in entry_path.glob("*.m4s"):
                    print(entry_file)
                    # entry_file = Path("E:/bcctest/140099078/140099078-1-30112.m4s")
                    file_size = entry_file.stat().st_size
                    split_num = file_size // (BUFFER_SIZE * 1024 * 1024) + 1 # 分割数量
                    print(split_num)

                    with entry_file.open(mode='rb') as f:
                        for i in range(split_num):
                            file_name = Path(str(entry_file) + "_{0}.temp".format(i))
                            with file_name.open(mode="wb") as p:
                                p.write(f.read(BUFFER_SIZE * 1024 * 1024))
                            
                    file_0 = Path(str(entry_file) + "_0.temp")
                    with file_0.open(mode="rb")as f:
                        bytes = f.read()
                    with file_0.open(mode="wb")as f:
                        bytes = bytes[9:]
                        f.write(bytes)

                    files = entry_path.glob("*.temp")

                    merge_file = Path(str(entry_file).split(".m4s")[0] + "_output.m4s")
                    print(str(merge_file))

                    with merge_file.open(mode="wb") as m:
                        for temp in sorted(files, key=lambda i: int(str(i.stem).split("m4s_")[1])):
                            with temp.open(mode="rb") as t:
                                m.write(t.read())
                            Path.unlink(temp)
                    input_files.append(merge_file)
                    
                filePathOrigin = Path(entry_path, "output.mp4")
                if Path.exists(filePathOrigin):
                    Path.unlink(filePathOrigin)
                cmdArgs = []
                cmdArgs.append(str(FFMPEG_PATH))
                for i in input_files:
                    cmdArgs.append("-i")
                    cmdArgs.append(str(i))
                cmdArgs.append("-codec")
                cmdArgs.append("copy")     
                cmdArgs.append(str(filePathOrigin))  
                out = subprocess.run(cmdArgs, capture_output=True, bufsize=4096)
                # print(out)
                for i in input_files:
                    Path.unlink(i)
                video_info = Path(entry_path, ".videoInfo")
                with video_info.open(mode='r', encoding='utf-8-sig') as vi:
                    row_data = json.load(vi)
                bvid = row_data.get("bvid")
                uname = row_data.get("uname")
                mainTitle = row_data.get("title")
                subTitle = row_data.get("tabName")
                videoTitle = mainTitle.replace('/', chr(ord('/') + 65248)).replace('\\', chr(ord('\\') + 65248))
                videoTitle += (" " + str(bvid)) if bvid else ""  
                videoSubtitle = subTitle.replace('/', chr(ord('/') + 65248)).replace('\\', chr(ord('\\') + 65248))
                cid = row_data.get("cid")
                print(cid)
                videoSubtitle += (" " + str(cid)) if cid != "" else ""
                currentOutputDir = outputDir
                if CREATE_UP_DIR:
                    currentOutputDir = Path(currentOutputDir, validPathName(uname))
                currentOutputDir = Path(currentOutputDir, validPathName(videoTitle))
                Path.mkdir(currentOutputDir, parents=True, exist_ok=True)
                filePathOutput = Path(currentOutputDir, validPathName(videoSubtitle) + '.mp4')
                filePathOrigin = Path(entry_path, "output.mp4")
                Path.rename(filePathOrigin, filePathOutput)
            except Exception as e:
                logging.error(e)
                logging.error("Failed to convert current video, skipping...")
                failedVideos.append({'path': str(entry_path), 'error': str(e)})
                continue
        
        res = ['true', failedVideos]
        return res            
    except Exception as e:
        logging.error(e)
        logging.error("Fatal error, converting failed.")
        res = ['false', failedVideos]
        return res