"""
write a python program that :
1 .defines a function named factorial that takes a number as an argument 
    and calculate its factorial using a loop or a recursion 
2. return the calculated factorial.
3. calls the function witha a sample number and prints the output.

"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))

fact = factorial(num)

print(f"Factorial of {num} is: {fact}")
