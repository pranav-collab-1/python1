def separate_even_odd(numbers):
    even = []
    odd = []

    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return even, odd


numbers = list(map(int, input("Enter numbers: ").split()))

even, odd = separate_even_odd(numbers)

print("Even numbers =", even)
print("Odd numbers =", odd)
