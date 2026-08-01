import math

a = float(input("Enter the x^2 coefficient: "))
b = float(input("Enter the x coefficient: "))
c = float(input("Enter the constant: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are:", x1, "and", x2)

elif d == 0:
    x = -b / (2*a)
    print("The roots are equal:", x)

else:
    print("The roots are imaginary.")
