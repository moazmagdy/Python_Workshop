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

    def __init__(self, height= 5, gender='unknown'):
        self.height = height    #In centimeters
        self.gender = gender    #Only male or female

    def is_tall(self):
        return self.height >= 30

aww = pet(height= 15, gender= "male")

print(aww.is_human,"\n",
        aww.owner,"\n",
        aww.__doc__, "\n",
        aww.height, "\n",
        aww.gender, "\n",
        aww.is_tall())