# Day 11: Dictionaries

# student = {"name" : "Manish", "age" : 25, "city" : "Mumbai"}
# print(student["name"])
# student["age"] = 26
# student["course"] = "Python"

# for key in student:
#     # print(key, ":" ,student[key])
#     print(student[key])


# dis = {"name" : "manish", "age" : 25, "goal" : "professional developer", "duration" : "3 month"}
# print(dis["name"])
# dis["duration"] = " 90 days"
# dis["Purpose"] = "Earning"

# for key in dis:
#     print(f"{key} : {dis[key]}")


# # CHALLENGE
# words = ["cat", "dog", "cat", "bird", "dog", "cat"]
# animal_count = {}

# for i in words:
#     if(i in animal_count):
#         animal_count[i] += 1
#     else:
#         animal_count[i] = 1
# print(animal_count)


# OPTIONAL CHANLLENGE

user_words = []

while True:
    user = input("Enter a word : ")
    if(user == "done"):
            break
    user_words.append(user)
    

word_counter = {}
for i in user_words:
    if(i in word_counter):
        word_counter[i] += 1
    else:
        word_counter[i] = 1
print(word_counter)