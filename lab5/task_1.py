import re, inspect, os.path


wordfile = input("Enter file for regex matching (local words.txt by default): ")
if(wordfile == ""): wordfile = "/words.txt"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))



with open(path + "/"+ wordfile) as f:
    data = f.read()

#matches a string that has an `'a'` followed by zero or more `'b'`'s
out = re.findall(r'.*a[b]*.*', data)

print(f"Words matching from file: {path}/{wordfile}")
for x in out:
    print(x)