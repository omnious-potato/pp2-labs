import re, inspect, os.path

wordfile = input("Enter file for input (local 'snakecamel' by default: ")
if(wordfile == ""): wordfile = 'snakecamel'

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

raw_data = r'{}'.format(data)


#idea is to capture position that will be needed for space, in this case in between lowercase and capital letter
#pattern = r'([a-z])([A-Z])' -- doesn't work for strings like 'ABC'

pattern = r'(?<!\b)(?=[A-Z])'
output = re.sub(pattern, ' ', data)

print(output)
