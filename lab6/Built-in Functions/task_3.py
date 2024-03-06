str = input("Enter  a string:")

bar = lambda s: s == ''.join(reversed(s))
print(bar(str))