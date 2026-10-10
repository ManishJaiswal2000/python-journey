# Day 10: Lists

# fruits = ["apple", "banana", "mango"]
# print(fruits[0])        # apple
# fruits.append("grape")  # add to the end
# print(len(fruits))      # 4

# for fruit in fruits:
#     print(fruit)


numbers = [1,2,3,4,5]
print(f"First item {numbers[0]} , Last item {numbers[4]} and Length of the list {len(numbers)}")

total = 0
for number in numbers:
    total = total + number
print(f"Total addup is {total}")


challenge_list = []
for i in range(3):
    user = int(input("Enter a number : "))
    challenge_list.append(user)

biggest = challenge_list[0]

for i in range(1, len(challenge_list)):
    if(biggest <= challenge_list[i]):
        biggest = challenge_list[i]
print(f"Largest number : {biggest}")