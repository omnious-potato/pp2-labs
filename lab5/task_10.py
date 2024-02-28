import re

print("Enter a string, send '.' symbol to end program: ")
while(True):
    camelCase = input()
    if(camelCase == '.'):
        break
    snake_case = (re.sub(r'(?<!^)([A-Z])', '_', camelCase)).lower()    
    print(snake_case)

