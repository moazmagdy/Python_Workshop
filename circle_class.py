import math
class circle():
    """
    A class for circles with radius and color as attributes.
    """

    is_shape = True

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def area(self):
        return round(math.pi * self.radius**2,2)

first_circle = circle(2,"blue")
second_circle = circle(5, "red")

first_circle.radius = 12

print("\n",
    'First circle attributes are:', first_circle.__dict__, "\n",
    'Second circle attributes are:', second_circle.__dict__,"\n",
    "First Circle area is:", first_circle.area(), "mm\u00b2")
