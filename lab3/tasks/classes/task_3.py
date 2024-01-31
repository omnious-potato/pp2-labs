from task_2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width=0):
        self.dim = 2
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

if __name__ == "__main__":
    print("Enter length and width for a Rectangle class instance (separated by a whitespace)")
    #s = Rectangle(*[input().split(" "))
    s = Rectangle(*[float(x) for x in input().split()])
    print("Area of such rectangle is ", s.area())
