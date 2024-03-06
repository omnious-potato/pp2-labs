list = input("Enter your list (newline is gonna be considered an end): ").split(' ')

result = 1
for x in [int(x) for x in list if x.lstrip('-').isdigit()]:
    result *= x
print(result)