import json
import subprocess
import shutil
from . import danmaku2ass
from pathlib import Path
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
    
    CREATE_UP_DIR = val['isUp'] # 如果需要将同一个up的视频放在单独一个文件夹,则改为True
    REMOVE_ORI = val['isDel']  # True if would like to delete origin cache file

    logging.info(CREATE_UP_DIR)

    vRoot = Path(downloadDir)
    logging.info("Current workspace: " + str(vRoot))

    try:
        for BVDir in list(filter(Path.is_dir, Path.iterdir(vRoot))):
            videoName = BVDir
            # Reach BV main directory
            logging.info("Current BV category: " + str(BVDir))
            # Multi-p. mark 0 for single 1 for multi
            multiFlag = 0
            if len(list(Path.iterdir(BVDir))) == 1:
                logging.warning("Current BV has only one Part")
            elif len(list(Path.iterdir(BVDir))) > 1:
                multiFlag = 1
                logging.warning("Current BV has more than one Part")
            else:
                logging.warning("Empty directory! Skipping...")
                continue

            for PDir in list(filter(Path.is_dir, Path.iterdir(BVDir))):
                partDir = PDir
                logging.info("Current Part category: " + str(partDir))
                # reach 这视频主文件夹中的一个分p
                # entry.json 文件路径
                entry_file = Path(PDir, "entry.json")
                # 读取json文件数据为字典
                with entry_file.open(mode='r', encoding='utf-8-sig') as f:
                    row_data = json.load(f)  # row_data是dict类型
                # 处理标题中的斜线 否则会被误判为下级目录
                videoTitle = row_data.get('title', 'no title').replace('/', chr(ord('/') + 65248)).replace('\\', chr(ord(
                    '\\') + 65248))
                videoSubtitle = row_data.get('page_data', 'no page data').get('download_subtitle', 'no subtitle').replace(
                    '/', chr(ord('/') + 65248)).replace('\\', chr(ord('\\') + 65248))
                videoQualityWidth = row_data.get('page_data', 'no page data').get('width', 'no width')
                videoQualityHeight = row_data.get('page_data', 'no page data').get('height', 'no height')
                upName = row_data.get("owner_name", "Undefined")
                logging.info("Current main title: " + videoTitle)
                logging.info("Current UPzhu: " + upName)
                logging.info("Current subtitle: " + videoSubtitle)
                logging.info("Current resolution: " + str(videoQualityWidth) + '*' + str(videoQualityHeight))
                # 转换后的danmaku.ass在与danmaku.xml同级目录下
                danmakuXMLPath = Path(PDir, "danmaku.xml")
                danmakuASSPath = Path(PDir, "danmaku.ass")

                danmaku2ass.Danmaku2ASS(str(danmakuXMLPath), 'Bilibili', str(danmakuASSPath), videoQualityWidth, videoQualityHeight, 0,
                            'Microsoft YaHei', 40)

                for M4SDir in list(filter(Path.is_dir, Path.iterdir(PDir))):  # 视频一般放在分p文件夹中的数字文件夹中，一般数字文件夹仅一个
                    sepPath = M4SDir
                    # os.chdir(sepPath)  # 进入分p的m4s文件夹
                    currentOutputDir = outputDir

                    if CREATE_UP_DIR:
                        currentOutputDir = Path(currentOutputDir, validPathName(upName))
                        logging.info("UPZhu category: " + str(currentOutputDir))

                    # newName = videoName + cDir + ".mp4"
                    if multiFlag == 0:
                        newName = validPathName(videoTitle)
                    elif multiFlag == 1:
                        newName = validPathName(videoSubtitle)
                    currentOutputDir = Path(currentOutputDir, validPathName(videoTitle))
                    filePathOutput = Path(currentOutputDir, newName + '.mp4')
                    danmakuPathOutput = Path(currentOutputDir, newName + '.ass')
                    Path.mkdir(currentOutputDir, parents=True, exist_ok=True)
                    if Path.exists(filePathOutput):
                        logging.warning("Video: " + newName + " already exist. skipping...")
                    else:
                        # 在此路径下调用cmd : ffmpeg -i video.m4s -i audio.m4s -codec copy Output.mp4
                        
                        # output.mp4的绝对路径
                        filePathVideoPart = Path(M4SDir, "video.m4s")
                        filePathAudioPart = Path(M4SDir, "audio.m4s")
                        filePathOrigin = Path(M4SDir, "Output.mp4")
                        if not Path.exists(filePathOrigin):
                            cmdArgs = []
                            cmdArgs.append(str(FFMPEG_PATH))
                            if(Path.exists(filePathVideoPart)):
                                cmdArgs.append("-i")
                                cmdArgs.append(str(filePathVideoPart))
                            if(Path.exists(filePathAudioPart)):
                                cmdArgs.append("-i")
                                cmdArgs.append(str(filePathAudioPart))
                            cmdArgs.append("-codec")
                            cmdArgs.append("copy")     
                            cmdArgs.append(str(filePathOrigin))    
                            
                            logging.info("Output.mp4 not exist, execute command: " + str(cmdArgs))                   
                            # out = subprocess.run([str(FFMPEG_PATH), "-i", str(Path(M4SDir, "video.m4s")), "-i", str(Path(M4SDir, "audio.m4s")), "-codec", "copy", str(Path(M4SDir, "Output.mp4"))], capture_output=True, bufsize=4096)
                            out = subprocess.run(cmdArgs, capture_output=True, bufsize=4096)
                            # logging.info("Output.mp4 not exist, execute command: " + str(out.args))
                            logging.info(out.stdout)
                        Path.rename(filePathOrigin, filePathOutput)
                        logging.info("Output video: " + str(currentOutputDir))

                    if Path.exists(danmakuPathOutput):
                        Path.unlink(danmakuPathOutput) 
                        logging.warning('Ass already exist, but replace it with new one.')
                    Path.rename(danmakuASSPath, danmakuPathOutput)
            
        logging.info("Congratulations! Convert successful.")

            
        if REMOVE_ORI:
            # remove 源文件夹
            for videoDir in list(filter(Path.is_dir, Path.iterdir(vRoot))):
                shutil.rmtree(videoDir)

        return 'true'

    except Exception as e:
        logging.error(e)
        logging.error("Sorry...Fail to convert.")
        return 'false'
