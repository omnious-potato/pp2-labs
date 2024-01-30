#Usual way would be just 'from foo import bar', but our import files start with digit, which causes problems
import importlib

one = importlib.import_module("1")
print("Enter mass in ounces: ", end="")
oz = input()
try:
    print(f"{int(oz)} oz = {one.gramsToOunces(oz)} g")
except Exception as e:
    print(f"Incorrect input!")



two = importlib.import_module("2")
print("Enter temperature in °F: ", end="")
temp = input()
try:
    print(f"{temp}°F = {two.farenheitToCelcius(temp):.2f}°C")
except Exception as e:
    print(f"Incorrect input!")


ten = importlib.import_module("10")
print("Enter list to extract unique elements: ", end="")
test = [x for x in input().split()]
try:
    print("Unique elements: ", ten.uniq(test))
except Exception as e:
    print(f"Incorrect input!")
