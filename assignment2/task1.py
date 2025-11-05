""" Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

"""

user_number = int(input("what is your number"))
if user_number == 0:
    print("enter a Natural number")
elif user_number % 2 ==0:
    print(f"{user_number}  is an  even number")
else:
    print(f"{user_number} is a odd number")

