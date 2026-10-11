# Day 22: Python Review and Gate 1 Check


# Calculate Total Expense
def sum_expense(dict):
    total = 0
    for item in dict:
        total += dict[item]
    result = f"{total:.2f}"
    return result
# print(sum_expense(dic_item))

def saving_expense(description, amount):
    with open("saving_expense.txt", "a") as f:
        f.write(f"{description},{amount}\n")
        
def load_expense():
    with open("saving_expense.txt", "r") as f:
        text = f.read()
    print(text)
    


dic_item = {}
while True:
    print("Menu : 1. Add expense, 2. View all, 3. Total, 4. Quit.")
    user = input("Please enter the type from above menu. What you want : ")
    try:
        if user == "Add expense":
            description = input("Please enter the description : ")
            amount = float(input("Enter the amount : "))
            dic_item[description] = amount
            saving_expense(description, amount)
        elif user == "View all":
            load_expense()
        elif user == "Total":
            print(sum_expense(dic_item))
        elif user == "Quit":
            break
    except ValueError:
        print("The entered amount is not a valid number.")

    



