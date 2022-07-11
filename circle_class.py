class circle():
    """
    A class for circles with radius and color as attributes.
    """
    is_shape = True

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

first_circle = circle(2,"blue")
second_circle = circle(5, "red")

print("\n",
    'First circle attributes are:', first_circle.__dict__, "\n",
    'Second circle attributes are:', second_circle.__dict__,"\n")
