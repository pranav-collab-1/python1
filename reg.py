import re
##print("\\d") 
##print(r"\d")
##print(re.fullmatch(r"\d+", "Ro2out5"))
##
##text = "I am learning Python"
##m = re.search(r"Python", text)
##print(m.group() if m else "Not found")
##
##text = "abc 123 xyz 456"
##m = re.search(r"\d+", text)
##print(m.group())

def menu():
    print("\nATM Menu")
    print("1. Check balance\n2. Withdrawal\n3. Deposit cash\n4. Exit\n")


def checkpin(entered_pin, correct_pin):
    return entered_pin == correct_pin


def show_balance(balance):
    print(f"Your current balance: {balance}")



def is_valid_amount(amount, balance):
    if amount <= 0:
        print("Invalid amount")
        return False
    elif amount % 100 != 0:
        print("Amount must be in multiples of 100")
        return False
    elif amount > balance:
        print("Insufficient balance!")
        return False
    return True


def withdrawal(balance, amount):
    balance -= amount
    print("Collect Your Cash!")
    return balance


def deposit(balance, amount):
    if amount <= 0:
        print("Invalid Deposit")
        return balance
    balance += amount
    print("Deposit successful!")
    return balance


correct_pin = "1234"
balance = 100000
attempts = 3
authenticated = False

while attempts > 0:
    entered_pin = input("Enter pin: ")
    if checkpin(entered_pin, correct_pin):
        print("Pin accepted")
        authenticated = True
        break
    else:
        attempts -= 1
        print(f"Wrong pin! Attempts left: {attempts}")

if not authenticated:
    print("Card blocked.")
else:
    while True:
        menu()
        choice = int(input("Enter Choice: "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            amount = int(input("Enter amount: "))
            if is_valid_amount(amount, balance):
                balance = withdrawal(balance, amount)
            show_balance(balance)
        elif choice == 3:
            amount = int(input("Enter amount: "))
            balance = deposit(balance, amount)
            show_balance(balance)
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid Choice!!!")
            
                       
        
                     
