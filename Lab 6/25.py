def find_largest(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

    return largest


numbers = list(map(int, input("Enter numbers: ").split()))

print(find_largest(numbers))
