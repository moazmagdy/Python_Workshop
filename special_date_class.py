"""
This class inherits from datetime.date class and allow user to increment date by n days.
"""
import datetime

class special_date(datetime.date):
    def add_days(self, n):
        return self + datetime.timedelta(n)

my_date = special_date(2022, 7, 20)
print(my_date.add_days(5))
