# Personal project. Developing an application to keep track of monthly finances.
# The user should be able to input their expenses and check it.
# As I progress here I will add the function to add income to compare it.

import tkinter as tk
from tkinter import *
# Create variable to store the expenses
expenses = [] 

# We will need 3 different frames
def screen(frame): 
    frame.tkraise()

# Define Frames
    screen_main = tk.Frame(root)
    screen_add = tk.Frame(root)
    screen_view = tk.Frame(root)

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


# Working on the GUI
# Function to execute option chosen
def execute_on_click ():
    option = txt.get()

    if option == "1" : 
        add_expense()
    elif option == "2" :
            view_expense()
    elif option == "3" : 
            print("Goodbye!")
    else :
            print("Invalid option")
            root.quit()

# Create root window
root = tk.Tk()
# Setting title
root.title("Expenses Tracker")
# Setting windows size
root.geometry('350x200')

# Working on the first screen
# Adding labels
lbl = Label(root, text = """ This is my expense tracker app. Here are your options :  
1 - Add expenses 
2 - Check expenses
3 - Exit """)
lbl.grid()

# Entry field for user input
txt = Entry(root, width=10)
txt.grid()

# Button to execute the option
exc_button = tk.Button(root, text = "Execute", command=execute_on_click) 
exc_button.grid()


# Working on the second screen
# Function to add expenses
def add_expense() : 
    try :
# Variables for data needed
        date = entry_date.get()
        category = entry_category.get()
        amount = entry_amount.get()
    
# Dictionary to store the data 
        expense = {
        "date" : date,
        "category" : category,
        "amount" : amount
    }
 # Clear fields
        entry_date.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)

        lbl_add_config(text = "Expense added !!")
    except ValueError:
        lbl_add_config(text = "Enter a valid value")

   lbl_add_config = tk.Label()

    
# Making the expenses dictionary global to reuse it in the next function
    expenses.append(expense)

lbl2 = tk.Frame(root)
lbl2.grid()

# Labels for the add expense function
tk.Label(lbl2, text="Which month did you spend?").grid()
entry_date = tk.Entry(lbl2)
entry_date.grid()

tk.Label(lbl2, text="On what did you spend? ex: food, trip").grid()
entry_category = tk.Entry(lbl2)
entry_category.grid()

tk.Label(lbl2, text="Wow much did you spend?").grid()
entry_amount = tk.Entry(lbl2)
entry_amount.grid()

# Working on the third screen


# Execute GUI
root.mainloop()