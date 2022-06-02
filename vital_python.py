""""
This is a text file to practice basic Python
Concepts
"""
# print(9%4)
# import math
# print(math.pow(4,2))
# print(math.ceil(9/5))
# import keyword
# print(keyword.kwlist)

# print("Here we use \\t \t to insert tab string!")
# print("Here we use \\n \n to add new line!")
# print("Here we use \\v \v to insert vertical tab!")
multiline_string = '''
During our vacation to San Francisco, we waited in a long line by
Powell St. Station to take the cable car. Tap dancers performed on
wooden boards. By the time our cable car arrived, we started looking
online for a good place to eat. We're heading to North Beach
'''
# print(multiline_string)

# print("Hi" + " MOHSEN! " * 3)

first_name = "Moaz"
last_name = "Magdy"

# print("Hi! {0} {1}, How are you?".format(first_name,last_name))
# print(first_name.lower())
# print(first_name.count('o'))
# print(first_name.find('z'))

# print(True + True)
# print(not True or False and True)

# print(6.0 >= 6)
# print('b' < 'c')

#While loop
# x = 10  #Step1: initialize the variable
# while x >= 1:   #Step2: Setup the while loop (While + variable + condition to run)
#     print(x)    #Step3: add Instructions
#     x -= 1      #Step4: define an incrementor --> Required to stop running forever.

#While loop to print the first number > 100 and divisible by 17
# x= 100
# while True:
#     if x % 17 == 0:
#         print(x)
#         break
#     else:
#         x += 1

#Find the Least common multiple
# x, y = 24, 36
# i = min(x,y)
# while True:
#     if (i % x == 0) and (i % y ==0):
#         print('The LCM is: ', i)
#         break
#     else:
#         i += 1
# import math
# while True:
#     x = input('Please enter a number to see if it\'s true square: ')
#     number = abs(int(x))
#     number_sqrt = math.sqrt(number)
#     if (number_sqrt - int(number_sqrt)) == 0:
#         print("{0} is a perfect square of {1}".format(number, int(number_sqrt)))
#         break

# print("one bedroom in the Bay Area is listed at $599,000.")
# offer = abs(int(input("Enter your first offer on the house.")))
# best = abs(int(input("Enter your best offer on the house.")))
# increment = abs(int(input("How much more do you want to offer each time?")))
# while True:
#     if offer >= 650000:
#         print('Your offer of', offer, 'has been accepted!')
#         break
#     else:
#         print("We're sorry, your offer of {} has not been accepted.".format(offer))
#         offer += increment

# for i in range(0,10,2):
#     print(i)
# name = "Moaz"
# for i in name:
#     for x in range(3):
#         print(i)

# questions = ["What's You're name?", "How old are you?"]

# for i in range(2):
#     ans = input(questions[i])
#     print("See! ", ans)


