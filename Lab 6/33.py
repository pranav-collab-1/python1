def merge_lists(list1, list2):
    return list1 + list2


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

print("Merged list =", merge_lists(list1, list2))
