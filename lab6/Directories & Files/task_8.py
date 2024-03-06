import os 

delete_path = input("Enter file path to delete it: ")

if(not os.access(delete_path, os.F_OK)):
    print("File doesn't exist!")
    quit()

if(os.path.isfile(delete_path)):
    if(not os.access(delete_path, os.R_OK)):
        print("No read permission!")
        quit()
    os.remove(delete_path)
    print(f"File {delete_path} is removed!")
else:
    print("Not a file provided!")