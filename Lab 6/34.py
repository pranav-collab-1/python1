def sum_even_positions(numbers):
    total = 0

    for i in range(0, len(numbers), 2):
        total += numbers[i]

    return total


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sum at even positions =", sum_even_positions(numbers))
