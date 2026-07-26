units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3.5
elif units <= 300:
    bill = (100 * 2) + (100 * 3.5) + (units - 200) * 4.5
else:
    bill = (100 * 2) + (100 * 3.5) + (100 * 4.5) + (units - 300) * 6

if bill < 200:
    bill = 200

if units <= 300:
    discount = 0
elif units <= 500:
    discount = bill * 0.05
else:
    discount = bill * 0.10

final_bill = bill - discount

print("Units Consumed :", units)
print("Bill Before Discount : Rs", bill)
print("Discount Amount : Rs", discount)
print("Final Payable Amount : Rs", final_bill)
