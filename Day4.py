#Day 4: Doing Maths and Using f-strings

price = int(input("Please enter the price of an item : "))
quantity = int(input("Please enter the quantity of an item : "))
total = price * quantity
print(f"{quantity} items at {price} each = {total}")