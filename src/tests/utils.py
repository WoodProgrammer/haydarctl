import glob

def check_file(file_path):
    if glob.glob(file_path):
        file_status = True
    else:
        file_status = False

    return file_status