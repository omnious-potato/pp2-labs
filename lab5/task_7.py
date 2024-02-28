import re, inspect, os.path

wordfile = input("Enter file for input (local 'snakecamel' by default): ")
if(wordfile == ""): wordfile = "snakecamel"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

raw_data = r'{}'.format(data)
snake_case = r'\b[a-z]+(_[a-z]+)*\b'

names = re.finditer(snake_case, raw_data)
for x in names: 
    print(x.group(0))
