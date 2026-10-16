def count_positive_negative(numbers):
    positive = 0
    negative = 0

    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1

    return positive, negative


numbers = list(map(int, input("Enter numbers: ").split()))

p, n = count_positive_negative(numbers)

print("Positive numbers =", p)
print("Negative numbers =", n)
