import os

filepath = input("Enter text file path: ")

if(not os.path.exists(filepath) or not os.access(filepath, os.R_OK)):
    print("This path doesn't exist or isn't accessible for reading!")
    quit()

if(not os.path.isfile(filepath)):
    print("Provided path isn't a file!")
    quit()

lines = 0
with open(filepath) as f:
    for x in f:
        lines += 1

print(f"Amount of lines in provided file: {lines}")