# matrix = [["Apple", "Banana", "Orange"], [4,5,6], [7,8,9]]
# print(matrix[1][2])

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j)

# employee_data = [["Name", "Age", "Department"],
#                 ["John Makee", 38, "Sales"],
#                 ["Ahmed", 29, "Logistics"],
#                 ["Mourad", 32, "Quality"]]

# for i in range(1, len(employee_data)):
#     print("Name: ", employee_data[i][0])
#     print("Age: ", employee_data[i][1])
#     print("Department: ", employee_data[i][2])
#     print("-------------------------")


from distutils.ccompiler import show_compilers


x = [[1,2],[4,5],[3,6]]
y = [[1,2,3,4],[5,6,7,8]]

result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

#Addition of two matrices
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         result[i][j]= x[i][j] + y[i][j]

#Multiplication of two matrices

# for i in range(len(x)):
#      for j in range(len(y[0])):
#         for k in range(len(y)):
#             result[i][j] += x[i][k] * y[k][j]
#         # print(i,j)
#         # print(result)
#         j += 1
#      i += 1

# print(result)

# import numpy as np
# print(np.dot(x,y))

# shopping = ["bread","milk", "eggs"]
# print(len(shopping))

# x = [1,2,3]
# # x.insert(1,5)
# x.remove(2)
# print(x)

# x = {"1": 1.2, "2": "Mohsen"}
# print(x.update(["2", "Ayman"]))

# movie = {
# "title": "The Godfather",
# "director": "Francis Ford Coppola",
# "year": 1972,
# "rating": 9.2
# }
# print(movie['title'])
# movie['earnings'] = 1000000
# print(movie['earnings'])

# emploee = [{"Name": "Ayman", "Age": 39, "Department": "Sales"},
# {"Name": "Anne", "Age": 32, "Department": "IT"},
# {"Name": "Mezo", "Age": 43, "Department": "Production"}
# ]

# employee = {1: {"Name": "Ayman", "Age": 39, "Department": "Sales"},
# 2: {"Name": "Anne", "Age": 32, "Department": "IT"},
# 3: {"Name": "Mezo", "Age": 43, "Department": "Production"}}

# for i in emploee:
#     print("Name:", i['Name'])
#     print("Age:", i['Age'])
#     print("Department:", i['Department'])
#     print('-'*30)

items = ['apple', 'orange', 'banana']
quantity = [5,3,2]
orders = zip(items,quantity)
# print(dict(orders))
# print(list(orders))
# print(tuple(orders))
# for i in orders:
#     print(i)

# print(list(dict(orders).values()))

# for i in dict(orders).items():
#     print(i)

# shopping = ('Egg', 'Apple', 'Orange')
# print(shopping+('Lemon','banana'))

# t = "Ahmed", 33, True, "Ahmed"
# t += "Mike", False
# print(t)
# print(t.count("Ahmed"))
# print(t.index(33))
# shopping = {"Apple", "Orange", "Apple", "Egg"}
# # print(shopping.union({'Cucumber','Garlic'}))
# print(shopping)
# shopping.add('Cucumber')

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5, 6}
# print(s1 | s2)
# print(s1 & s2)
# print(s1-s2)
# print(s2- s1)
# s1.difference_update(s2)
# print(s1, s2)
# print(s1.issubset(s2))
# print(s1 <= s2)
print(s2 >= s2)