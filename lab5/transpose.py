matrix = [[1, 2, 3],[4, 5, 6]]
transpose = []
for i in range(len(matrix[0])):
 new_row = []
 for row in matrix:
 new_row.append(row[i])
 transpose.append(new_row)
print(transpose)
