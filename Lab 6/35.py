def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(total):
    return total / 3


def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def find_result(m1, m2, m3):
    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        return "PASS"

    return "FAIL"


roll = input("Enter roll number: ")
name = input("Enter name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = calculate_total(m1, m2, m3)
average = calculate_average(total)
grade = find_grade(average)
result = find_result(m1, m2, m3)

print("\n--- STUDENT RESULT ---")
print("Roll Number:", roll)
print("Name:", name)
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)
