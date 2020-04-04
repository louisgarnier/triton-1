import os

def CreateDirectory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass