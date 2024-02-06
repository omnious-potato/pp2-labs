import math

sides = int(input("Number of sides: "))
side_length = float(input("Length of a side: "))

if(sides < 3 or side_length <= 0):
    print("Invalid input!")
else:
    area = sides * 1/4.0 * math.pow(side_length, 2) * math.tan(math.pi / sides)
    print(f"Area of the regular polygon: {area:.4f}")