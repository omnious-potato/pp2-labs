class PowerfulString:   
    def __init__(self, data=""):
        self.data = data
    
    def getString(self):
        self.data = input()

    def printString(self):
        print(self.data)



if __name__ == "__main__":
    s = PowerfulString()
    print("getStringMethod input: \t\t", end="")
    s.getString()
    print("printStringMethod output: \t", end="")
    s.printString()