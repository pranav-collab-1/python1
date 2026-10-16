def find_average(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total / len(numbers)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Average =", find_average(numbers))
