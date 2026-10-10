# Day 9: The while Loop

# count = 1
# while(count <=3):
#     print(count)
#     count += 1
# print("Done")


# while True:
#     answer = input("Type quit the stop")
#     if(answer == 'quit'):
#         break


# count = 10
# while(count != 0):
#     print(count)
#     count = count - 1
# print("Liftoff!")

count = 1
while count < 4:
    pwd = input("Enter a password : ")
    if(pwd == "python123"):
        print("Access granted")
        break
    count += 1
else:
    print("Too many attempts")