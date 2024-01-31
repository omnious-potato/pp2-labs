from __future__ import annotations #to allow typehinting a Point class type into dist() method for type mismatch handling


class Point:
    def __init__(self, coords):        
        self.dim = 0
        self.coordinates = []
        
        for x in coords:
            self.dim += 1
            self.coordinates.append(float(x))

    
    def show(self):
        print("( ", end="")
        for x in self.coordinates:
            print(x, end=" ")
        print(")")

    
    def move(self, new_coords):
        if len(new_coords) != len(self.coordinates):
            print(f"Dimensionality mismatch! Point has {len(self.coordinates)} coordinates, but got {len(new_coords)} arguments.")
        else:
            for i in range(0, len(new_coords)):
                self.coordinates[i] = float(new_coords[i])


    def dist(self,  p: Point):
        sum  = .0
        if len(self.coordinates) != len(p.coordinates):
            print(f"Dimensionality mismatch!")
        else:
            for i in range(0, len(self.coordinates)):
                sum += (p.coordinates[i] - self.coordinates[i])**2
            return sum ** (0.5)


if __name__ == "__main__":
    
    p1 = Point(*[input("Initialize point with coordinates (separated by whitespace): ").split()])
    p1.show()
    
    p1.move(*[input("Move that point to a new location: ").split()])
    p1.show()
    
    p2 = Point(*[input("Initialize second point with coordinates (separated by whitespace): ").split()])
    p2.show()

    print(f"Distance between two points: {p2.dist(p1)}")
    
