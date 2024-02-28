import re, inspect, os.path

wordfile = input("Enter file for regex matching (local words.txt by default): ")
if(wordfile == ""): wordfile = "words.txt"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

raw_data = r'{}'.format(data)
#matches a string that has an 'a' followed by anything, ending in 'b'
out = re.findall(r'.*a.*b', data)

#print(out)

if(out is not None):
    for x in out:
        print(x)
else:
    print("There isn't any sequences!")

