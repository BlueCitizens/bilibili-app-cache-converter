import json
import os
import subprocess
import shutil
from . import danmaku2ass
from . import hello, bye
from pathlib import Path, PurePath
import logging

logging.basicConfig(level=logging.DEBUG,  # logging level
                    filename='test.log',
                    format='%(asctime)s-[%(filename)s-->line:%(lineno)d]-[%(levelname)s]%(message)s')

def convert(val):

    try:
        downloadDir = val['path']  # cache file root (should be tv.danmaku.bili/download/...)
        outputDir = val['output']  # output video file root
        REMOVEOri = False  # True if would like to delete origin cache file

        ffmpeg_path = Path.cwd()
        # os.chdir(downloadDir)
        directory = Path(__file__)
        logging.info("Current workspace: " + str(ffmpeg_path))
        logging.info("Current workspace: " + str(directory))
        # current_path = os.path.abspath(__file__)
        logging.info(hello.test())
        path = Path(downloadDir)

        for BVDir in list(filter(Path.is_dir, Path.iterdir(path))):
            videoName = BVDir
            # videoMainDir = PurePath.joinpath(videoNameDir)
            # os.chdir(videoMainDir)  # reach 视频主文件夹
            # videoMainDirPath = os.getcwd()
            logging.info("当前BV目录: " + str(BVDir))
            # 多p标记 0为单p 1为多p
            multiFlag = 0
            if len(list(Path.iterdir(BVDir))) == 1:
                logging.warning("当前视频仅有一个分p")
            elif len(list(Path.iterdir(BVDir))) > 1:
                multiFlag = 1
                logging.info("当前视频多于一个分p")
            else:
                logging.warning("空的目录")

            for PDir in list(filter(Path.is_dir, Path.iterdir(BVDir))):
                partDir = PDir
                logging.info("当前分p目录: " + str(partDir))
                # os.chdir(partDir)  # reach 这视频主文件夹中的一个分p
                # path = os.getcwd()
                # print(os.listdir())
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
                logging.info("当前视频主标题: " + videoTitle)
                logging.info("当前分p副标题: " + videoSubtitle)
                logging.info("当前分p视频分辨率: " + str(videoQualityWidth) + '*' + str(videoQualityHeight))

                # 转换后的danmaku.ass在与danmaku.xml同级目录下
                danmakuXMLPath = Path(PDir, "danmaku.xml")
                danmakuASSPath = Path(PDir, "danmaku.ass")

                danmaku2ass.Danmaku2ASS(str(danmakuXMLPath), 'Bilibili', str(danmakuASSPath), videoQualityWidth, videoQualityHeight, 0,
                            'Microsoft YaHei', 40)

                
                for M4SDir in list(filter(Path.is_dir, Path.iterdir(PDir))):  # 视频一般放在分p文件夹中的数字文件夹中，一般数字文件夹仅一个
                    sepPath = M4SDir
                    # os.chdir(sepPath)  # 进入分p的m4s文件夹

                    # newName = videoName + cDir + ".mp4"
                    if multiFlag == 0:
                        newName = videoTitle
                    elif multiFlag == 1:
                        newName = videoTitle + "-" + videoSubtitle
                    filePathOutput = Path(outputDir, newName + '.mp4')
                    danmakuPathOutput = Path(outputDir, newName + '.ass')

                    if Path.exists(filePathOutput):
                        logging.warning("视频 " + newName + " 已存在 跳过")
                    else:
                        # 在此路径下调用cmd : ffmpeg -i video.m4s -i audio.m4s -codec copy Output.mp4
                        # logging.info(Path.cwd())
                        out = subprocess.run(["./ffmpeg/bin/ffmpeg.exe", "-i", str(Path(M4SDir, "video.m4s")), "-i", str(Path(M4SDir, "audio.m4s")), "-codec", "copy", str(Path(M4SDir, "Output.mp4"))], capture_output=True, bufsize=4096)
                        # logging.info(out.a)
                        # output.mp4的绝对路径
                        filePathOrigin = os.path.join(M4SDir, "Output.mp4")
                        Path.rename(filePathOrigin, filePathOutput)

                    if os.path.exists(danmakuPathOutput):
                        logging.warning('检测到已存在ass弹幕文件 将其删除处理')
                        os.remove(danmakuPathOutput)
                    Path.rename(danmakuASSPath, danmakuPathOutput)
            
        logging.info("转换成功")
        return 'true'
    
        if REMOVEOri:
            # remove 源文件夹
            os.chdir(downloadDir)
            directory = os.getcwd()
            for videoNameDir in list(filter(os.path.isdir, os.listdir())):
                videoNameDirPath = os.path.join(directory, videoNameDir)
                shutil.rmtree(videoNameDirPath)
    except:
        logging.error("转换失败")
        return 'false'
