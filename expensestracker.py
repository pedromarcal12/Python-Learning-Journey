# Personal project. Developing an application to keep track of monthly finances.
# The user should be able to input their expenses and check it.
# As I progress here I will add the function to add income to compare it.

import tkinter as tk
from tkinter import *

# Create variable to store the expenses
expenses = [] 

# Create root window
root = tk.Tk()
# Setting title
root.title("Expenses Tracker")
# Setting windows size
root.geometry('350x200')

# We will need 3 different frames
def screen(frame): 
    frame.tkraise()
 # Define Frames
screen_main = tk.Frame(root)
screen_add = tk.Frame(root)
screen_view = tk.Frame(root)

for frame in (screen_main, screen_add, screen_view):    
        frame.grid(row=0, column=0, sticky='nsew')

# Working on the first screen

# Adding labels
lbl = Label(screen_main, text = """ This is my expense tracker app. Here are your options :  
1 - Add expenses 
2 - Check expenses
3 - Exit """)
lbl.grid()

# Entry field for user input
txt = Entry(screen_main, width=10)
txt.grid()

# Function to execute option chosen
def execute_on_click ():
    option = txt.get()

    if option == "1" : 
        screen(screen_add)
    elif option == "2" :
            screen(screen_view)
    elif option == "3" : 
           root.quit()
    else :
            print("Invalid option, try again.")
            

# Button to execute the option
exc_button = tk.Button(screen_main, text = "Execute", command=execute_on_click) 
exc_button.grid()


# Working on the second screen
# Labels for the add expense function
tk.Label(screen_add, text="Which month did you spend?").grid()
entry_date = tk.Entry(screen_add)
entry_date.grid()

tk.Label(screen_add, text="On what did you spend? ex: food, trip").grid()
entry_category = tk.Entry(screen_add)
entry_category.grid()

tk.Label(screen_add, text="How much did you spend?").grid()
entry_amount = tk.Entry(screen_add)
entry_amount.grid()

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
        expenses.append(expenses)

 # Clear fields
        entry_date.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)

        lbl_add.config(text = "Expense added !!")
    except ValueError:
        lbl_add.config(text = "Enter a valid value")

lbl_add = tk.Label(screen_add, text="")
lbl_add.grid()

btn_save = tk.Button(screen_add, text="Save Expense", command=add_expense)
btn_save.grid()

btn_back = tk.Button(screen_add, text="Back", command=lambda:screen(screen_main))
btn_back.grid()

# Working on the third screen

lbl_expense = tk.Label(screen_view, text="Here are your expenses")
lbl_expense.grid()

# Method for viewing the expenses in total and monthly
def view_expense() : 
    # If no data in expenses, show a message
    if not expenses:
        lbl_expense.config(text="No expenses added yet")
        return

    result = "Total of your expenses"

    # Creating the monthly view for expenses
    monthly_expenses = {}   

    for i, exp in enumerate(expenses, start=1):
        result += f"{i}. {exp['date']} - {exp['category']} - ${exp['amount']}\n"
        month = exp['date']
        monthly_expenses[month] = monthly_expenses.get(month, 0) + exp['amount']

    result += "\nTotal by Month:\n"
    for month, total in monthly_expenses.items():
        result += f"{month}: ${total:.2f}\n"

    lbl_expense.config(text=result)

btn_back_view = tk.Button(screen_view, text="Back to Menu", command=lambda: screen(screen_main))
btn_back_view.grid()

# Execute GUI
screen(screen_main)
root.mainloop()