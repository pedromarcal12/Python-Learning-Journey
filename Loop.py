# Questions taken from the book "The Self-Taught Programmer"

def tasks() : 
    print("Task 1 - Print three different strings")    
    print("A \nP \nX")

    print("Task 2 - Print a message if var is less than 10 and other message if greater or equal to 10")
    var = 10 
    if var < 10 :
        print ("{var} is indeed less than 10!")
    if var >= 10 :
        print (f"{var} is indeed more or equal to 10!")

    print("Task 3 - Print a message if var is less than or equal to 10, another message if greater than 10 but less or equal to 25 and another message if greater then 25")
    var2 = 26 
    if var2 <= 10 :
        print(f"{var2} is less or equal to 10")
    elif var2 > 10 and var2 <= 25 :
        print(f"{var2} is greater than 10 and less or equal to 25")
    else :
        print(f"{var2} is greater than 25!")

    print("Task 4 - Create a program that divides two variables and prints the remainder")
    print ("Tell me the first number")
    num1 = int(input())
    print("Tell me another number")
    num2 = int(input())
    result = num1 % num2
    print(f"Here is the remainder : {result}")

    print("Task 5 - Create a program that takes two variables, divides them and print the quotient")
    result2 = num1 // num2 
    print("Here is the quotient " f"{result2}")

    print("Task 6 - Write a program with a var age with a int value that print different messages depending on the age value")
    print("Tell me your age: ")
    age = int(input())
    if age <= 10 :
        print("You are very young!")
    elif age > 11 and age <= 22 :
        print("You are young but not as much!")
    elif age > 23 and age <= 40:
        print("Getting older!")
    else :
        print("Sorry too old!!")


# Main program with for loop to ask if user wants to run again
for i in range(100):  # Maximum 100 runs to prevent infinite loops
    tasks()
    print("\n" + "="*50)
    repeat = input("Do you want to run the tasks again? (yes/no): ").lower()
    if repeat not in ['yes', 'y']:
        print("Goodbye!")
        break


n1 = input("Tell me your name")
n2 = input("Tell me your surname")

answer = "Your full name is {} {}".format(n1, n2)
print(answer)

