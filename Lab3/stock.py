stock = 50

while stock > 0:
    sold = int(input("Enter the number of units sold (-1 to stop): "))

    if sold == -1:
        print("Inventory management stopped.")
        break

    if sold > stock:
        print("Not enough stock available.")
        continue

    stock = stock - sold
    print("Available stock:", stock)

    if stock <= 10 and stock > 0:
        print("Reorder Alert")

if stock == 0:
    print("Stock is empty.")
