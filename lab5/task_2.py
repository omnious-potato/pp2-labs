import re, inspect, os.path

wordfile = input("Enter file for regex matching (local words.txt by default): ")
if(wordfile == ""): wordfile = "/words.txt"

py_filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(py_filename))

print(f"Regex matching from file: {path}/{wordfile}")

with open(path + "/"+ wordfile) as f:
    data = f.read()

#matches a string that has an `'a'` followed by two to three `'b'`
#to output a whole word (string) with a match not just a string piece '.*' (any) prefix and '[^b]*' (anything except containing 'b') suffix
out = re.finditer(r'.*a[b]{2,3}[^b]*$', data, re.MULTILINE)

if(out is not None):
    for x in out:
        print(x)
else:
    print("There isn't any matches!")