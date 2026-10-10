# Day 13: Functions with Several Parameters and Defaults

def make_coffee(drink, size="medium"):
    return f"One {size} {drink}"

print(make_coffee("latte"))
print(make_coffee("mocha", "large"))
print(make_coffee("tea", "small"))


def calculate_bill(price, quantity, gst_rate=18):
    sub_total = price * quantity
    gst = sub_total * (gst_rate / 100)
    return sub_total + gst

total = calculate_bill(50, 3)
print(f"Total bill: {total:.2f}")
print(f"Total bill: {calculate_bill(50, 3, 12):.2f}")


def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too low"
    else:
        return "too high"

print(check_guess(15, 12))


def biggest_number(numbers):
    if not numbers:
        return None
    ans = numbers[0]
    for number in numbers:
        if ans < number:
            ans = number
    return ans

print(biggest_number([-5, -2, -9]))
print(biggest_number([]))