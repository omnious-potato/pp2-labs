import os

given_path = input("Enter path: ")

if(not os.path.exists(given_path)):
    print("Given path doesn't exist!")
else:
    print(f"Directory portion (absolute): \"{os.path.abspath(given_path)}\"")
    print(f"Directory portion (given, may include relative): \"{os.path.dirname(given_path)}\"")
    if os.path.isfile(given_path):
        print(f"Filename portion: {os.path.basename(given_path)}")