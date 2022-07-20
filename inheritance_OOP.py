class pet():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class dog(pet):
    is_feline = False

class cat(pet):
    is_feline = True

my_cat = cat("Aww", 12)
print(my_cat.is_feline)