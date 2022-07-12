"""
This script creates a class of my pets with common attributes.
"""
class pet():
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them.
    """
    is_human = False
    owner = "Moaz Magdy"

    def __init__(self, height, gender='unknown'):
        self.height = height    #In centimeters
        self.gender = gender    #Only male or female

    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least

aww = pet(height= 15, gender= "male")
aww.is_tall(30)

print(aww.is_human,"\n",
        aww.owner,"\n",
        aww.__doc__, "\n",
        aww.height, "\n",
        aww.gender, "\n",
        aww.is_tall(30))