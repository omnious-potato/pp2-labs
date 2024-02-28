import re, inspect, os.path

wordfile = input("Enter file for input (local lorem_ipsum.txt by default): ")
if(wordfile == ""): wordfile = "lorem_ipsum.txt"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

raw_data = r'{}'.format(data)
#replace all occurrences of space, comma, or dot with a colon.
pattern = re.compile(r'[ ,.]+')

raw_data = re.sub(pattern, ':', raw_data)

print(raw_data)