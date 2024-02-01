def square_generator(n):
    val = 1
    
    while val <= n:
        yield val**2
        val += 1


if __name__ == "__main__":
    N = int(input("Enter up to which number squares are gonna be generated: "))
    obj = square_generator(N)
    
    #Ensure this gives generator class
    print(type(obj))
    
    print("Iterating over generator using next()")
    it = iter(obj)
    try:
        while True:
            item = next(it)
            print(item, end=" ")
    except StopIteration:
        pass
    print()

    
    #Alternatively we can iterate over generated generator like this:
    print("Iterating over generator using for/in ")
    obj = square_generator(N)
    for x in obj:
        print(x, end=" ")
    print()