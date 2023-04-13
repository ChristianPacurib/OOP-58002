class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def diameter(cls, diameter):
        return cls(diameter / 2)

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius



Circle = Circle(radius = float(input("Input the intended radius of the circle:")))
print("The area of the given Circle:", Circle.area())
print("The perimeter of the given Circle:", Circle.perimeter())