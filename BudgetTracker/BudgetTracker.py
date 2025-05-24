import json


def add_expenses(expenses,description,amount):
    amount=float(amount)
    expenses.append({"description":description, "amount":amount})
    print(f"Add Expense: {description}, amount: {amount}")

def get_total_budget(expenses):
    return sum(expense['amount'] for expense in expenses)

def get_balance(budget,expenses):
    return budget-get_total_budget(expenses)
def show_budget_details(budget,expenses):
    print(f"amount {amount}")
    print("Expenses")
    for expense in expenses:
        print(f"- {expense['description']}:{expense['amount']}")
    print(f"Total Budget: {get_total_budget(expenses)}")
    print(f"Remaining Budget: {get_balance(budget,expenses)}")


def load_budget_data(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data['initial_budget'],data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0,[]
    
def save_budget_details(filepath,initial_budget,expenses):
    data={
        "initial_budget":initial_budget,
        "expenses":expenses
    }
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)

print("Welcome to Budget Tracker")
filepath="Data.json"
initial_budget,expenses=load_budget_data(filepath)
budget=initial_budget
if initial_budget==0:
    initial_budget=float(input("Enter Initial_Budget"))
expenses=[]
while True:
    print("\nWhat would you like to do")
    print("1: Add expense amount")
    print("2: Show budget details")
    print("3: Exit")
    choice=input("Enter (1/2/3): ")

    if choice=="1":
        description=input("Enter description: ")
        amount=float(input("Enter amount: "))
        add_expenses(expenses,description,amount)
    
    elif choice=="2":
        show_budget_details(budget,expenses)

    elif choice=="3":
        save_budget_details(filepath, initial_budget, expenses)
        print("Exiting Budget App!! GoodBye")
        break
    else:
        print("Invalid Input")
        continue