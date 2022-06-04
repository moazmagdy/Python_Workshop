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

#Addition of two matrices

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10,11,12],[13,14,15],[16,17,18]]

result= [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[i])):
        result[i][j]= x[i][j] + y[i][j]

print(result)