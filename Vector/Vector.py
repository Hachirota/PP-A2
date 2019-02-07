import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return("({},{})").format(self.x,self.y)

    def __add__(self, other):
        productx = self.x + other.x
        producty = self.y + other.y

        return Vector(productx,producty)

    def __sub__(self, other):
        subx = other.x * -1
        suby = other.y * -1

        productx = self.x + subx
        producty = self.y + suby

        return Vector(productx, producty)

    def __mul__(self, other):
        if type(other) == Vector:
            return (self.x * other.x) + (self.y * other.y)

        if type(other) == int:
            return Vector(self.x * other, self.y * other)

    def magnitude(self):
        return math.sqrt(self.x^2 + self.y^2)

def main():
    vectora = Vector(1,3)
    vectorb = Vector(2,5)

    vectorc = vectora * 5

    print(vectorc.__str__())


if __name__ == '__main__':
    main()
