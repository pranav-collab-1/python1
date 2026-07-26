correct=9366
attempts=0
while attempts<3:
    pin=int(input("Enter You 4 digit AIM pin:"))
    if pin==correct:
        print("Access Granted For Transaction!")
    else:
        attempts += 1
        print("wrong pin,you have only left with chances",3-attempts)
