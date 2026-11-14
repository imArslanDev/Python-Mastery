"""
Question 1: Create a list and Print first, last, and middle index from list 
using both positive and negative indexing where appropriate.
"""

marks = [1, 2, 3, 4, 5, 500, 1, 2, 3, 4, 5]

n = len(marks)
print(f"First element = {marks[0]}")
print(f"Last element = {marks[-1]}")
print(f"Middle element = {marks[n//2]}")  # This is Floor Division Divide + Round Floor


"""
Question 2: Create a list of 5 numbers. Replace the second and fourth elements of this
list with the number 0 using indexing. Print the updated list.
"""

numList = [10, 20, 30, 40, 50]
numList[1] = 0
numList[3] = 0
print(numList)
