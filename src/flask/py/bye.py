from . import hello
from pathlib import Path

def bye():
    if hello.test().is_file():
        return True
    else:
        return False