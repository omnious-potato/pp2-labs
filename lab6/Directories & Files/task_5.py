import os

filepath = input("Enter text file path: ")

mode = 'w'

if(os.path.exists(filepath)):
    if(not os.path.isfile(filepath)):
        print("Not a file!")
        quit()
    else:
        print("Warning: file already exists, new changes will be appended to the existing content!")
        mode = 'a'


whole_input = input("Enter a list to write to file (separated by whitespace): ")
list = whole_input.split(' ')
print(list)


with open(filepath, mode) as f:
    for x in list: f.write(x + '\n') 
