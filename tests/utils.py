import glob
import os

def check_file(file_path):
    if glob.glob(file_path):
        file_status = True
    else:
        file_status = False

    return file_status

def check_file_size(file_path):
    return os.path.getsize(file_path)