# Day 16: Saving Data to Files

# Demo
with open("notes.txt", "w") as f:
    f.write("Hello\n")

with open("notes.txt", "r") as f:
    text = f.read()
print(text)


# Exercise
with open("profile.txt", "w") as f:
    f.write("My name is Manish Jaiswal.\nMy goal is to complete the roadmap journey.")

with open("profile.txt", "r") as f:
    text = f.read()
print(text)


# Challenge
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

save_best(5)
print(load_best())