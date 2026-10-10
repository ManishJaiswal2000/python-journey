# Day 14: Weekly Mini-Project, Guess the Number (Part 1)

# PART1: Random secret value
import random
secret = random.randint(1, 100)
# print(secret)   # uncomment ONLY for testing


# PART2: check_guess function
def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too low"
    else:
        return "too high"


# PART3: The game loop
attempt = 1

while attempt <= 7:
    user = int(input("Enter your guess: "))
    result = check_guess(user, secret)

    if result == "correct":
        print("Congratulations!")
        print(f"You got it in {attempt} tries!")
        break
    else:
        print(result)
    attempt += 1
else:
    print(f"Out of tries. The secret number was {secret}")