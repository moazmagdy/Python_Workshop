class country():
    def __init__(self, name= "Unspecified", population= None, size_kmsq= None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq
    
    def size_milesq(self, conversion_factor = 0.621371):
        return self.size_kmsq * conversion_factor

egypt = country(name= "Egypt", population= 10**8, size_kmsq= 10**6)

print(egypt.size_milesq(0.62))
print(egypt.__dict__)