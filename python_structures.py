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


x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10,11,12],[13,14,15],[16,17,18]]

result= [[0,0,0],
        [0,0,0],
        [0,0,0]]

#Addition of two matrices
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         result[i][j]= x[i][j] + y[i][j]

#Multiplication of two matrices

for i in range(len(result)):
     for j in range(len(x[0])):
         for v in range(len(x[0])):
             result[i][j] += x[i][j+v] * y[i+v][j]
             print(result)
             print(i,j,v)
         j += 1
     i += 1

print(result)