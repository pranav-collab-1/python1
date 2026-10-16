def search_element(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i

    return -1


numbers = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter element to search: "))

print("Position =", search_element(numbers, key))
