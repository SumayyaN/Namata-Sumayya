#   Assignment 3
#QN:Write a program to handle errors, the program should ask for two number using input and then divides them. Use an infinite loop to keep asking until a valid input is provide.

print("This program divides two numbers.")

while True:
    try:
        number_one = int(input("Enter the first number:\n"))
        number_two = int(input("Enter the second number:\n"))

        def divider(a, b):
            return a / b

        result = divider(number_one, number_two)
        print("Your answer is",result)
        break  

    except ValueError:
        print("Invalid input. Please enter integers only")
    except ZeroDivisionError :
        print("Cannot divide by zero")

   
