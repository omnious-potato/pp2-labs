import math

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
l = [base, height]


if(base <= 0 or height <= 0):
    print("Invalid input!")
else:
    area = math.prod(l)
    print(f"Area of the parallelogram: {area:.4f}")