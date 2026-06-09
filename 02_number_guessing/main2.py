import random

try:
    top_of_range = int(input("Type a number: "))
except ValueError:
    print("Please type a valid number next time.")
    quit()

if top_of_range <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0

print(f"I am thinking of a number between 1 and {top_of_range}")

while True:
    guesses += 1

    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")

print(f"You got it in {guesses} guesses")