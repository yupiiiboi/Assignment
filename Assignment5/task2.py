"""
        Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
numbers = list(range(1, 11))

first_five = numbers[0:5]

first_five.reverse()

print(f"Original list: {numbers}")
print(f"Extracted first five elements: {numbers[0:5]}")
print(f"Reversed extracted elements: {first_five}")
