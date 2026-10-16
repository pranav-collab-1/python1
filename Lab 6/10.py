def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)


a = int(input())
b = int(input())

print(find_gcd(a, b))
print(find_lcm(a, b))
