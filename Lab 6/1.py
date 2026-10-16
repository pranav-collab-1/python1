def square_cube(n):
 square = n * n
 cube = n * n * n
 return square, cube
n = int(input("Enter number: "))
square, cube = square_cube(n)
print(square)
print(cube)
