# Finished Project 1
#Day 17: High Score in Your Game

# PART1: Random secret value
import random
secret = random.randint(1, 100)
# print(secret)   # uncomment ONLY for testing


# PART2: Get number from user
def get_number():
    while True:
        try:
            number = int(input("Enter a number from 1 to 100 : "))
            if 1 <= number and number <= 100:
                return number
            else:
                print("Please enter a number from 1 to 100")
        except ValueError:
            print("That is not a number")


# PART3: check_guess function
def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too low"
    else:
        return "too high"


# PART4: save_best and load_best - to keep the high score
def save_best(n):
    with open("best_score.txt", "w") as f:
        f.write(str(n))

def load_best():
    try:
        with open("best_score.txt", "r") as f:
            text = f.read()
        return int(text)
    except FileNotFoundError:
        return None


# PART5: The game loop
attempt = 1
best = load_best()

if best is None:
    print("Your current score will be the best high score.")
else:
    print(f"Best so far: {best} tries")

while attempt <= 7:
    user = get_number()
    result = check_guess(user, secret)

    if result == "correct":
        print("Congratulations!")
        if (best is None) or (attempt < best):
            save_best(attempt)
            print("New best!")
        else:
            print(f"Current best is {best}")
        print(f"You got it in {attempt} tries!")
        break
    else:
        print(result)
    attempt += 1
else:
    print(f"Out of tries. The secret number was {secret}")