def even_generator(n):
    val = 0
    while val <= n:
        if(val < n):
            yield str(val) + ", "
        else:
            yield str(val) + "\n"
        val += 2



if __name__ == "__main__":
    N = int(input("Enter up to which number even numbers are gonna be listed (separated by commas): "))
    obj = even_generator(N)

    for x in obj:
        print(x, end="")
    