import string

names = list(string.ascii_uppercase)
for i in range(0, len(names)):
    names[i] += '.txt'

for x in names:
    open(x, 'a').close()