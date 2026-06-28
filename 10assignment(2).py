import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius
c = Circle(7)
print("Diameter =", c.diameter())
print("Area =", c.area())
print("Circumference =", c.circumference())