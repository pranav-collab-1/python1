grocery_list = ["Rice", "Milk", "Eggs", "Bread"]

print("Initial Grocery List:")
print(grocery_list)

new_item = input("Enter a new grocery item to add: ")
grocery_list.append(new_item)

remove_item = input("Enter the grocery item to remove: ")

if remove_item in grocery_list:
    grocery_list.remove(remove_item)
    print(remove_item, "removed successfully.")
else:
    print(remove_item, "not found in the list.")

print("\nFinal Grocery Shopping List:")
print(grocery_list)
