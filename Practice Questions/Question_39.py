"""
Question:  Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""

# Solution


def find_max(num1, num2, num3):
    largest = (
        num1 if (num1 >= num2 and num1 >= num3)
        else (num2 if num2 >= num3 else num3)
    )
    print(f"Largest Num: {largest}")


find_max(12, 34, 50)
