import os
import shutil


def delete_files_from_server(path, file_name):
    files = os.listdir(path)
    for f in files:
        p = os.path.join(path, f)
        if os.path.isdir(p):
            print(p)
            if f in file_name:
                continue
            elif f not in file_name:
                shutil.rmtree(p, True)
            else:
                delete_files_from_server(p, file_name)
        else:
            if f not in file_name:
                os.remove(p)
    return print(os.listdir(path))


def delete_files_from_repository(path, file_name):
    files = os.listdir(path)
    for f in files:
        print(f)
        p = os.path.join(path, f)
        if os.path.isdir(p):
            print(p)
            if f in file_name:
                shutil.rmtree(p, True)
            else:
                delete_files_from_repository(p, file_name)
        else:
            if f in file_name:
                os.remove(p)
    return print(os.listdir(path))