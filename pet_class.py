"""
This script creates a class of my pets with common attributes.
"""

class pet():
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them.
    """
    def __init__(self, height= 5, gender= ["male", "female"]):
        self.height = height
        self.gender = gender

    is_human = False
    owner = "Moaz Magdy"

aww = pet(height= 15, gender='male')

print(aww.is_human,"\n",
        aww.owner,"\n",
        aww.__doc__, "\n",
        aww.height, "\n",
        aww.gender)