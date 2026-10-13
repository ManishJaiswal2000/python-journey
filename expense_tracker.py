# Day 22: Python Review and Gate 1 Check


# Calculate Total Expense
def sum_expense(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    result = f"{total:.2f}"
    return result

def saving_expense(description, amount):
    with open("saving_expense.txt", "a") as f:
        f.write(f"{description},{amount}\n")
        

def load_expenses():
    expenses = []
    try:
        with open("saving_expense.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                part = line.rsplit(",", 1)
                expenses.append({"description": part[0], "amount": float(part[1])})
    except FileNotFoundError:
        pass
    return expenses
    
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet")
    for expense in expenses:
        print(f"{expense['description']} : {expense['amount']:.2f}")



expenses = load_expenses()
while True:
    print("Menu : 1. Add expense, 2. View all, 3. Total, 4. Quit.")
    choice = input("Enter 1, 2, 3, or 4 : ")
    if choice == "1":
        description = input("Please enter the description : ")
        try:
            amount = float(input("Enter the amount : "))
        except ValueError:
            print("The entered amount is not a valid number.")
        else:
            expenses.append({"description": description, "amount": amount})
            saving_expense(description, amount)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        print(sum_expense(expenses))
    elif choice == "4":
        break
    else:
        print("Invalid choice")

    

    



