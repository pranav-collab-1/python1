def simple_interest(p, r, t):
    return (p * r * t) / 100


def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount - p


p = float(input())
r = float(input())
t = float(input())

print(simple_interest(p, r, t))
print(compound_interest(p, r, t))
