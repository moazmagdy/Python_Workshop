class person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @full_name.setter   #setter alows assigning new values to property.
    def full_name(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last

class baby(person):
    def speak(self):
        print('Blah blah blah')

class adult(person):
    def speak(self):
        print('Hello my name is {}'.format(self.first_name))

class talktive_adult(adult):
    def speak(self):
        super().speak()
        print('It is a pleasure to meet you!')

my_baby = baby('Mohsen', 'Ali')
my_adult = adult('Fawzy', 'Mohamed')
my_talktive = talktive_adult('Marwa', 'Magdy')

my_baby.speak()
my_adult.speak()
my_talktive.speak()