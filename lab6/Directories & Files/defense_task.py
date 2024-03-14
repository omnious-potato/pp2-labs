import sys
import string

names = list(string.ascii_uppercase)
for i in range(0, len(names)):
    names[i] += '.txt'


list = []

for i in range(len(names)):
    list.append(i+1)

    sys.stdout = open(names[i], 'w')
    print(list)


    # print(list)
    # with open(names[i], 'w') as f:
        # f.write('[')
        # for j in range(len(list) - 1):
            # f.write(str(list[j]) + ', ')
        # f.write(str(list[-1]))
        # f.write(']')