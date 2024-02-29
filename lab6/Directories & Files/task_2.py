import os, stat


path = input("Enter path to check for various access types: ")

print(f"Does path \"{path}\" exist? -- {os.access(path,os.F_OK)}")
print(f"Is path \"{path}\" readable? -- {os.access(path,os.R_OK)}")
print(f"Is path \"{path}\" writable? -- {os.access(path,os.W_OK)}")
print(f"Is path \"{path}\" executable? -- {os.access(path,os.X_OK)}")

