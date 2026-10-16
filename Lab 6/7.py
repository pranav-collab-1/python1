def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev


def is_palindrome(n):
    if n == reverse_number(n):
        return True
    else:
        return False


n = int(input())
print(is_palindrome(n))
