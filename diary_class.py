import datetime
class diary():
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas
    
    @staticmethod
    def format_date(date):
        return  date.strftime('%d-%b-%y')

    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_christmas(self):
        return self.format_date(self.christmas)

my_diary = diary(datetime.date(1991, 1, 1),
                 datetime.datetime(2020, 12, 25))

if __name__ == '__main__':
    print(my_diary.show_birthday(), '\n',
        my_diary.show_christmas())