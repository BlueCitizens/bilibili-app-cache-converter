# This is a sample Python script.
import json
# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
import shutil
import logging

logging.basicConfig(level=logging.DEBUG,  # 日志级别
                    format='%(asctime)s-[%(filename)s-->line:%(lineno)d]-[%(levelname)s]%(message)s')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    downloadDir = "E:/bilicache/download"  # 存放从手机复制而来的文件夹的地方
    outputDir = "E:/converted"  # 存放最终mp4文件的地方
    REMOVEOri = False  # 如果需要将源文件删除，将其更改为True

    os.chdir(downloadDir)
    directory = os.getcwd()
    logging.info("Current workspace: " + directory)

    for videoNameDir in list(filter(os.path.isdir, os.listdir())):
        videoName = videoNameDir
        videoMainDir = os.path.join(directory, videoNameDir)
        os.chdir(videoMainDir)  # reach 视频主文件夹
        videoMainDirPath = os.getcwd()
        logging.info("进入视频目录: " + videoMainDirPath)
        # 多p标记 0为单p 1为多p
        multiFlag = 0
        if len(os.listdir()) > 1:
            logging.warning("当前视频多于一个分p")
            multiFlag = 1

        # 遍历分p文件夹
        for cDir in list(filter(os.path.isdir, os.listdir())):
            eachPartPath = os.path.join(directory, videoNameDir, cDir)
            os.chdir(eachPartPath)  # reach 这视频主文件夹中的一个分p
            path = os.getcwd()
            print(os.listdir())
            # entry.json 文件路径
            path = path + "/entry.json"
            # 读取json文件数据为字典
            with open(path, "r", encoding='utf-8-sig') as f:
                row_data = json.load(f)  # row_data是dict类型
            # 处理标题中的斜线 否则会被误判为下级目录
            videoTitle = row_data.get('title', 'no title').replace('/', chr(ord('/') + 65248)).replace('\\', chr(ord(
                '\\') + 65248))
            videoSubtitle = row_data.get('page_data', 'no page data').get('download_subtitle', 'no subtitle').replace(
                '/', chr(ord('/') + 65248)).replace('\\', chr(ord('\\') + 65248))
            logging.info("当前视频主标题: " + videoTitle)
            logging.info("当前分p副标题: " + videoSubtitle)

            for digitFolder in list(filter(os.path.isdir, os.listdir())):  # 视频一般放在分p文件夹中的数字文件夹中，一般数字文件夹仅一个
                sepPath = os.path.join(directory, videoNameDir, cDir, digitFolder)
                os.chdir(sepPath)  # 进入分p的m4s文件夹

                # newName = videoName + cDir + ".mp4"
                if multiFlag == 0:
                    newName = videoTitle + ".mp4"
                else:
                    newName = videoTitle + "-" + videoSubtitle + ".mp4"
                filePathOfOutput_newName_with_NewPath = os.path.join(outputDir, newName)

                if os.path.exists(filePathOfOutput_newName_with_NewPath):
                    logging.warning("视频 " + newName + " 已存在 跳过")
                    break

                # 在此路径下调用cmd : ffmpeg -i video.m4s -i audio.m4s -codec copy Output.mp4

                subprocess.call('ffmpeg -i video.m4s -i audio.m4s -codec copy Output.mp4', shell=True)
                # output.mp4的绝对路径
                filePathOfOutput_oldName = os.path.join(directory, videoNameDir, cDir, digitFolder, "Output.mp4")

                os.rename(filePathOfOutput_oldName, filePathOfOutput_newName_with_NewPath)

    if REMOVEOri:
        # remove 源文件夹
        os.chdir(downloadDir)
        directory = os.getcwd()
        for videoNameDir in list(filter(os.path.isdir, os.listdir())):
            videoNameDirPath = os.path.join(directory, videoNameDir)
            shutil.rmtree(videoNameDirPath)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
