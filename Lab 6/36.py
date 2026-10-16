PIN = "1234"


def check_pin():
    for attempt in range(3):
        entered = input("Enter PIN: ")

        if entered == PIN:
            return True

        print("Incorrect PIN.")

    return False


def is_valid_amount(amount):
    return amount > 0


def withdraw(balance, amount):
    if not is_valid_amount(amount):
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")

    return balance


def deposit(balance, amount):
    if not is_valid_amount(amount):
        print("Invalid amount.")
    else:
        balance += amount
        print("Deposit successful.")

    return balance


if check_pin():
    balance = 5000.0

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance =", balance)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)

        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)

        elif choice == "4":
            print("Thank you.")
            break

        else:
            print("Invalid choice.")
else:
    print("Card blocked after three incorrect attempts.")
