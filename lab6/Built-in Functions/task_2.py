str = input("Enter  a string:")



foo = lambda s: (len(list(filter(lambda char: char.islower(), str))), \
                 len(list(filter(lambda char: char.isupper(), s))))

high, low = foo(str)

print(f"Uppercase letters:{high}\nLowercase letters:{low}")