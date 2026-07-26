p = input("Enter Product Name:")
q = float(input("Enter Quantity of Product:"))
price = float(input("Enter Price:"))
Tax = (price*5)/100
Total = (q*price)+ Tax
print(p)
print(q)
print(price)
print("The Total Amount :",Total)
