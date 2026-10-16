def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        return True
    else:
        return False


n = int(input())
print(is_perfect(n))
