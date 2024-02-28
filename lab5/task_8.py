import re, inspect, os.path

wordfile = input("Enter file for input (local 'lorem_ipsum_longer.txt' by default -- single line of text, multiple sentences with first word after comma capitalized ): ")
if(wordfile == ""): wordfile = "lorem_ipsum_longer.txt"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

raw_data = r'{}'.format(data)
pattern = r'(?=[A-Z])'

split_str = [s for s in re.split(pattern, raw_data) if s]

for x in split_str: 
    print(x)
