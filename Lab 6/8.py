def is_armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    if total == original:
        return True
    else:
        return False


n = int(input("Enter number: "))
print(is_armstrong(n))
