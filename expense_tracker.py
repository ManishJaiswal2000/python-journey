# Day 22: Python Review and Gate 1 Check


# Calculate Total Expense
def sum_expense(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    result = f"{total:.2f}"
    return result
# print(sum_expense(dic_item))

def saving_expense(description, amount):
    with open("saving_expense.txt", "a") as f:
        f.write(f"{description},{amount}\n")
        

def load_expenses():
    expenses = []
    try:
        with open("saving_expense.txt", "r") as f:
            for line in f:
                striped_line = line.strip()
                part = striped_line.split(",")
                dict_item = {"description": part[0], "amount": float(part[1])}
                expenses.append(dict_item)
    except FileNotFoundError:
        return expenses
    return expenses
# print(load_expenses())
    
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet")
    for expense in expenses:
        print(f"{expense['description']} : {expense['amount']:.2f}")
        

expenses = load_expenses()
while True:
    print("Menu : 1. Add expense, 2. View all, 3. Total, 4. Quit.")
    user = input("Please enter the type from above menu. What you want : ")
    try:
        if user == "Add expense":
            description = input("Please enter the description : ")
            amount = float(input("Enter the amount : "))
            expenses.append({"description": description, "amount": amount})
            saving_expense(description, amount)
        elif user == "View all":
            view_expenses(expenses)
        elif user == "Total":
            print(sum_expense(expenses))
        elif user == "Quit":
            break
    except ValueError:
        print("The entered amount is not a valid number.")

    



