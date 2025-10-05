# Personal project. Developing an application to keep track of monthly finances.
# The user should be able to input their expenses and check it.
# As I progress here I will add the function to add income to compare it.

# Create variable to store the expenses
expenses = [] 

# Function to add expenses
def add_expense() : 
# Variables for data needed
    date = input("Which month did you spend ")
    category = input("What you spend the food on. I.e : food, transport ")
    amount = float(input("How much have you spent "))
    
# Dictionary to store the data 
    expense = {
    "date" : date,
    "category" : category,
    "amount" : amount
}

# Making the expenses dictionary global to reuse it in the next function
    expenses.append(expense)


# Method for viewing the expenses in total and monthly
def view_expense() : 
    # If no data in expenses, show a message
    if len(expenses) == 0 :
        print("Nothing added yet.")
        return

    # If data in expenses, show the expenses
    else :
        print("Here are your monthly expenses")
        print(expenses)

    # Creating the monthly view for expenses
    monthly_expenses = {}   
    for i, exp in enumerate(expenses, start = 1) :
        print(f"{i}. {exp['date']} - {exp['category']} - {exp['amount']}")

    # Loop through the expenses and add the amount into the monthly expenses variable
        month = exp["date"]
        if month in monthly_expenses :
            monthly_expenses[month] += exp["amount"]
        else :
            monthly_expenses[month] = exp["amount"]
    print("Expenses by month:")       
    for month, amount in monthly_expenses.items() :
        print(f"{month}: {amount}")


# Main program with while loop to ask if user wants to run again
while True : 
    print("""This is my expense tracker app. Here are your options :  
1 - Add expenses 
2 - Check expenses """)

    answer = int(input("Tell me the option : "))


    if answer == 1 :
        add_expense()
    elif answer == 2 :
        view_expense()
    else:
        print("Goodbye!")
        break


