# Day 23: Classes and Objects

# class Expense:
#     def __init__(self, description, amount):
#         self.description = description
#         self.amount = amount

#     def show(self):
#         return f"{self.description} : {self.amount:.2f}"

# tea = Expense("Tea", 20)
# coffee = Expense("Coffee", 30.5)

# print(tea.show())
# print(coffee.amount)



# EXCERISE
class Expense:
    def __init__ (self, description, amount):
        self.description = description
        self.amount = amount

    def show(self):
        return f"{self.description} : {self.amount:.2f}"

tea = Expense("Tea", 15)
coffee = Expense("Coffee", 20)
milk = Expense("Milk", 25)

list_data = []
list_data.append(tea)
list_data.append(coffee)
list_data.append(milk)

for obj in list_data:
    print(obj.show())

def total_expense(list_data):
    total_sum = 0
    for obj in list_data:
        total_sum += obj.amount
    return total_sum
print(f"Total sum of the list data is {total_expense(list_data):.2f}")


# CHALLENGE
class Student:
    def __init__(self,name):
        self.name = name
        self.marks = []

    def add_mark(self,mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        else:
            count = 0
            total = 0
            for mark in self.marks:
                count += 1
                total += mark
            return (total/count)

s1 = Student("Manish")
s1.add_mark(1)
s1.add_mark(2)
s1.add_mark(3)
s1.add_mark(4)
s1.add_mark(5)
print(s1.average())


s2 = Student("Ajay")
s2.add_mark(6)
s2.add_mark(7)
s2.add_mark(8)
s2.add_mark(9)
s2.add_mark(10)
print(s2.average())

    




