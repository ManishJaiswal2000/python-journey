# Day 12: Functions

def greet(name):
    return f"Hello!, {name}"

name = "Manish"
msg = greet(name)

print(msg)
print(greet("Jaiswal"))


# print vs return
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_return(2, 3)   # x is 5
y = add_print(2, 3)    # prints 5, but y is None
print(x)
print(y)


# EXERCISE
def square(n):
    return n * n
# print(square(5))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(5))
print(is_even(10))


def word_count(text):
    list_value = list(text.split(" "))
    answer = {}

    for item in list_value:
        if item in answer:
            answer[item] += 1
        else:
            answer[item] = 1
    return answer

print(word_count("the cat the dog"))


# CHALLENGE
def biggest_number(numbers):
    ans = numbers[0]

    for number in numbers:
        if ans < number:
            ans = number
    return ans

print(biggest_number([-5, -2, -9]))