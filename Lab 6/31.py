def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result


numbers = list(map(int, input("Enter numbers: ").split()))

print("List without duplicates =", remove_duplicates(numbers))
