numbers = [10, 15, 20, 25, 30, 35, 40]

books = [
    "Python Programming",
    "Java",
    "Data Structures",
    "C",
    "Machine Learning"
]

even_numbers = [num for num in numbers if num % 2 == 0]
print("a) Even Numbers:")
print(even_numbers)

squares = [num ** 2 for num in numbers]
print("\nb) Squares of all Numbers:")
print(squares)

long_titles = [title for title in books if len(title) > 10]
print("\nc) Book Titles with more than 10 characters:")
print(long_titles)

even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("\nd) Squares of Even Numbers:")
print(even_squares)
