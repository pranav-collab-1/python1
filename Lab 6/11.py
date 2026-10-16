def largest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


a = int(input())
b = int(input())
c = int(input())

print(largest_of_three(a, b, c))
