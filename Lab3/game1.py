import random
target = random.randint(1, 50)
print(f"(Debug) Target number is: {target}")   

guess = 0
attempts = 0
while guess != target:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct!")
print(f"You guessed it in {attempts} attempts.")
