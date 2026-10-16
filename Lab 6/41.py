def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def sum_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == n


while True:
    print("\n1. Factorial")
    print("2. Prime Check")
    print("3. Sum of Digits")
    print("4. Palindrome Check")
    print("5. Armstrong Check")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "6":
        print("Program ended.")
        break

    n = int(input("Enter number: "))

    if choice == "1":
        print("Factorial =", factorial(n))

    elif choice == "2":
        print("Prime =", is_prime(n))

    elif choice == "3":
        print("Sum of digits =", sum_digits(n))

    elif choice == "4":
        print("Palindrome =", is_palindrome(n))

    elif choice == "5":
        print("Armstrong =", is_armstrong(n))

    else:
        print("Invalid choice.")
