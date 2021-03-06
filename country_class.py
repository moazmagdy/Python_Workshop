class country():
    has_flag = True
    has_government = True

    def __init__(self, country_name= "Unspecified", population= None, size_kmsq= None):
        self.name = country_name
        self.population = population
        self.size_kmsq = size_kmsq
    
    def __str__(self):
        return  "Country name is: {0}, and total population: {1}".format(self.name, self.population)

    def size_milesq(self, conversion_factor = 0.621371):    #Instance method
        return self.size_kmsq * conversion_factor

    @staticmethod
    def is_african(country_name):
        return country_name in ['Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'South Africa']

    @classmethod
    def independent(cls):
        return cls.has_flag and cls.has_government

    @classmethod
    def convert_to_milesq(cls, country_name, population, size_kmsq):
        size_milesq = size_kmsq * 0.386102
        return cls(country_name, population, size_milesq)

egypt = country(country_name= "Egypt", population= 10**8, size_kmsq= 10**6)

# print(egypt.size_milesq(0.62))
# print(egypt.__dict__)
# print(egypt, egypt.is_african("Egypt"))
# print(country.independent())
