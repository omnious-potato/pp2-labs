class Shape:
    def __init__(self):
        self.length   = .0  
        self.dim    = 0
    def area(self):
        return .0
        # if(self.dim == 0 or self.dim == 1):
        #     return .0
        # else:
        #     return float("NaN")


#subclass
class Square(Shape):
    def __init__(self, length:float = .0):
        self.length = length
        self.dim = 2
    
    #Does the same thing as constructor above, just in a separate method like asked in task lists
    def init(self, length):
        self.length = length

    def area(self):
        return self.length**self.dim
    

if __name__ == "__main__":
    shape = Shape()
    print("Default area for Shape class: ", shape.area())
    square = Square()
    print("Default area for Square class: ", square.area())

    print("Enter square length to initialize it via constructor: ", end="")
    square = Square(float(input()))
    print("Area of that square is ", square.area())


    print("Change square length via \".init\" method: ", end="")
    square.init(float(input()))
    print("Area of updated square is: ", square.area())
    
