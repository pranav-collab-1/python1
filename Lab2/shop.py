while True:
    a = int(input("Enter the Purchased Amount: "))
    b = int(input("Enter Membership type 1.Regular 2.Silver 3.Gold 4.Platinum: "))

    if b == 1:
        if a < 500:
            print("No discount")
        else:
            print("Original Amount:", a)
            print("Discount Amount:", (a * 5) / 100)
            d = (a * 5) / 100

            if (a - d) < 1000:
                print("Amount Should Pay:", a - d + 50)
            else:
                print("Amount Should Pay:", a - d)

    elif b == 2:
        if a > 10000:
            print("Original Amount:", a)
            print("Discount Amount:", (a * 10) / 100 + 500)
            e = (a * 10) / 100 + 500

            if (a - e) < 1000:
                print("Amount Should Pay:", a - e + 50)
            else:
                print("Amount Should Pay:", a - e)

        elif (a < 10000) and (a >= 500):
            print("Original Amount:", a)
            print("Discount Amount:", (a * 10) / 100)
            e = (a * 10) / 100

            if (a - e) < 1000:
                print("Amount Should Pay:", a - e + 50)
            else:
                print("Amount Should Pay:", a - e)

        else:
            print("No discount")

    elif b == 3:
        if a > 10000:
            print("Original Amount:", a)
            print("Discount Amount:", (a * 15) / 100 + 500)
            f = (a * 15) / 100 + 500

            if (a - f) < 1000:
                print("Amount Should Pay:", a - f + 50)
            else:
                print("Amount Should Pay:", a - f)

        elif (a < 10000) and (a >= 500):
            print("Original Amount:", a)
            print("Discount Amount:", (a * 15) / 100)
            f = (a * 15) / 100

            if (a - f) < 1000:
                print("Amount Should Pay:", a - f + 50)
            else:
                print("Amount Should Pay:", a - f)

        else:
            print("No discount")

    elif b == 4:
        if a > 10000:
            print("Original Amount:", a)
            print("Discount Amount:", (a * 20) / 100 + 500)
            g = (a * 20) / 100 + 500

            if (a - g) < 1000:
                print("Amount Should Pay:", a - g + 50)
            else:
                print("Amount Should Pay:", a - g)

        elif (a < 10000) and (a >= 500):
            print("Original Amount:", a)
            print("Discount Amount:", (a * 20) / 100)
            g = (a * 20) / 100

            if (a - g) < 1000:
                print("Amount Should Pay:", a - g + 50)
            else:
                print("Amount Should Pay:", a - g)

        else:
            print("No discount")

    else:
        print("Invalid Membership Type")
