import subprocess, os
from pathlib import Path


my_file = Path("./py/hello.py")


def test():
    # out = subprocess.run("./ffmpeg/bin/ffmpeg.exe -version", capture_output=True)
    # return(out.stdout)
    return os.path.abspath('./')