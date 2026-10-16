def sort_list(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list =", sort_list(numbers))
