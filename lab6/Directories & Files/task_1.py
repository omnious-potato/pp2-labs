import os

def list_directories(path, supress_errors=False):
    if(not os.path.exists(path) and not supress_errors):
        print(f"Path {path} doesn't exist")
        return
    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):
            print(f"D\t{dir_path}")


def list_files(path, supress_errors=False):
    if(not os.path.exists(path) and not supress_errors):
        print(f"Path {path} doesn't exist")
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            print(f"F\t{file_path}")

def list_files_directories(path, supress_errors=False):
    if(not os.path.exists(path) and not supress_errors):
        print(f"Path {path} doesn't exist")
    list_directories(path, True)
    list_files(path, True)

mode = input("Enter mode - D(directories)/F(files)/A(all): ")

s = input("Enter directory: ")
if(mode == 'D'):
    list_directories(s)
if(mode == 'F'):
    list_files(s)
if(mode == 'A'):
    list_files_directories(s)

        




