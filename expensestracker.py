# Personal project. Developing an application to keep track of monthly finances.
# The user should be able to input their expenses and check it.
# As I progress here I will add the function to add income to compare it.

# Create variable to store the expenses
expenses = [] 

# Function to add expenses
def add_expense() : 
# Variables for data needed
    date = input("Which day did you spend")
    category = input("What you spend the food on. I.e : food, transport")
    amount = float(input("How much have you spent"))
    
# Dictionary to store the data 
    expense = {
    "date" : date,
    "category" : category,
    "amount" : amount
}
# Making the expenses dictionary global to reuse it in the next function
    expenses.append[expense]


def view_expense() : 
    if len(expenses) == 0 :
        print("Nothing added yet.")
        return

    else :
        print("Here are your monthly expenses")
        print(expenses)




answer = input("""This is my expense tracker app. Here are your options :  
1 - Add expenses 
2 - Check expenses""")

if answer == "1" :
    add_expense()
else : 
    view_expense()


