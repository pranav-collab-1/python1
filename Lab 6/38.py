def electricity_bill(units):
    if units <= 100:
        return units * 3

    elif units <= 300:
        return 100 * 3 + (units - 100) * 5

    else:
        return 100 * 3 + 200 * 5 + (units - 300) * 8


units = int(input("Enter units consumed: "))

print("Electricity bill = Rs.", electricity_bill(units))
