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