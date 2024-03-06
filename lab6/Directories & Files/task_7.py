import os

source_path = input("Enter file path to copy from: ")
destination_path = input("Enter path to copy to: ")

source_path = os.path.expanduser(source_path)
destination_path = os.path.expanduser(destination_path)


if(not os.path.isfile(source_path)):
    print("Source path isn't a file!")
    quit()

if(not os.path.exists(source_path) or not os.access(source_path, os.R_OK)): 
    print("Source file doesn't exist or unreadable!")
    quit()

#Handling case where we provided target folder and didn't provide name 
if(os.path.isdir(destination_path)):
    destination_path += "/" + os.path.basename(source_path)


print(destination_path)
os.makedirs(os.path.dirname(destination_path), exist_ok=True)
with open(destination_path, 'wb') as dst:
    with open(source_path, 'rb') as src:
        dst.write(src.read())