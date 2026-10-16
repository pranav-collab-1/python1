def print_table(n, limit=10):
    for i in range(1, limit + 1):
        print(n, "x", i, "=", n * i)


n = int(input("Enter number: "))
print_table(n)
