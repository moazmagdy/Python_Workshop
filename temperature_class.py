class temp():
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < - 460:
            raise ValueError('Temperatures less than -460F are not possible')
        self.celsius = (value - 32) * 5/9

temp = temp(5)
temp.fahrenheit = -470
print(temp.celsius)