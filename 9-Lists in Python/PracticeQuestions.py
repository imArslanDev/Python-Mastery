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



"""
Question 3: Find a largest and smallest number in a list without using built-in functions.
"""
numsList = [2, 3, 12, 56, 78, 90, 100, 340, 120, -100, 4500]

largest = numsList[0]
smallest = numsList[0]

for value in numsList:
    if value > largest:
        largest = value

    if value < smallest:
        smallest = value

print(f"Smallest Value: {smallest}")
print(f"Largest Value: {largest}")

"""
Question 4: Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

reversed_list = []
def reverse_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])


randomList = [2,45,65,20,40,50]

print(reverse_list(randomList))
print(reversed_list)