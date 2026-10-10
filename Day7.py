# Day 7: Combining Conditions with and, or, not

age = int(input("Enter your age : "))

if age < 1:
    print("That is invalid")
elif 1 <= age and age < 13:
    print("Child")
elif 13 <= age and age <= 19:
    print("Teenager")
elif 20 <= age and age <= 59:
    print("Adult")
elif 60 <= age and age <= 100:
    print("Senior")
else:
    print("Enter a valid age")



# Challenge
# a = 10
# b = 5
# print(a > 5 and b > 10)
# print(a > 5 or b > 10)
# print(not a > 5)