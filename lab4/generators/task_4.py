def squares(a, b):
    val = a
    while(val <= b):
        yield val**2
        val += 1


if __name__ == "__main__":
    a, b = input("Enter two numbers to output all squares in [a, b] range: ").split(" ")
    obj = squares(int(a), int(b))
    print(type(obj))


    print(f"Listing squares in [{a},{b}]")
    for x in obj:
        print(x, end=" ")
    print()

