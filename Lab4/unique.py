n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    item = input("Enter element: ")
    lst.append(item)

unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)
print("Original List:", lst)
print("List after removing duplicates:", unique_list)
