import math

degrees = float(input("Degrees: "))

#radians = (degrees / 180.0 * math.pi) 
radians = math.radians(degrees)

print(f"Radians: {radians:.6f}")