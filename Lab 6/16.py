def count_digits(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count


n = int(input())
print(count_digits(n))
