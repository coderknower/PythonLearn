

class triangle:
    def __init__(self, base, height):
        self.base= base
        self.height= height

    def area(self):
        return 0.5*self.base*self.height

ob = triangle(5,12)

print("The area of triangle is",ob.area())


