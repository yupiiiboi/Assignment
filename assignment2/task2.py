"""Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""

number_sum = 0
for i in range(1,50):
    number_sum+= i
    
print(f"The sum of numbers from 1-50 is = {number_sum}")


