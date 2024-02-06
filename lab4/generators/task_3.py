def divisibility_gen(n):
    val = 1
    while val <= n:
        #if(val % 4 == 0 and val % 3 == 0):
        #4 and 3 are coprime so if x mod 4 = 0 and x mod 3 = 0 then x mod 12 = 0
        if(val % 12 == 0):
            yield val
        val += 1


def foo(n):
    obj = divisibility_gen(n)
    L = list(obj) #after that generator is exhausted and wouldn't yield any values
    print(f"Printing list made from generator object: {L}")


    obj = divisibility_gen(n)
    print(f"Printing generator values using iteration: ", end="")
    for x in obj:
        print(x, end=" ")
    print()



if __name__ == "__main__":
    foo(int(input("Enter N: ")))

    