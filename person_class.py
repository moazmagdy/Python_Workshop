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

customer = person("Moaz", "Magdy")
customer.full_name = 'Ayman Hamdy'
print(customer.full_name)