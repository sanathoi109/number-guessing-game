import random

print("Welcome to the Number Guessing Game!")

print("\nChoose difficulty level:")
print("1. Easy (1 - 50)")
print("2. Medium (1 - 100)")
print("3. Hard (1 - 200)")

choice = input("Enter your choice: ")

if choice == "1":
    number = random.randint(1, 50)
elif choice == "2":
    number = random.randint(1, 100)
elif choice == "3":
    number = random.randint(1, 200)
else:
    print("Invalid choice. Game starting with Medium difficulty.")
    number = random.randint(1, 100)

attempts = 0

print("\nStart guessing!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Correct! You guessed the number.")
        print("Attempts taken:", attempts)
        break