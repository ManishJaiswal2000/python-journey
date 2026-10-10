# Day 15: Making the Game Crash-Proof

# Step 1: basic try / except
try:
    number = int(input("Enter a number: "))
    print("You entered", number)
except ValueError:
    print("That is not a number")


# Step 2: keep asking until valid
while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered", number)
        break
    except ValueError:
        print("That is not a number")


# EXERCISE
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

print(get_number())