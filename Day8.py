# Day 8: Repeating with for Loops

for i in range(1,6):
    print(i)


total = 0
for j in range(1,11):
    total += j
print(total)


# Challenge
number = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")