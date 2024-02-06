import  math # yet to find why do we need math package at all


height = float(input("Height: "))
base_1 = float(input("Base first: "))
base_2 = float(input("Base second: "))

bases = [base_1, base_2]

print("Area of trapezoid: ", (math.fsum(bases))/2.0 * height)
