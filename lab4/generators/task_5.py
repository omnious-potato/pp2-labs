def linear_descending_gen(n):
    val = int(n)
    while(val >= 0):
        yield val
        val -= 1

if __name__ == "__main__":
    obj = linear_descending_gen(input("Enter N: "))
    print(list(obj))