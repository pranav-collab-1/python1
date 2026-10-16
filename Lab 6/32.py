def total_marks(*subjects):
    total = 0

    for mark in subjects:
        total += mark

    return total


marks = list(map(int, input("Enter marks: ").split()))

print("Total marks =", total_marks(*marks))
