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

new_list = []


def reverse_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        new_list.append(lst[i])
    return new_list


randomList = [2, 45, 65, 20, 40, 50]

print(reverse_list(randomList))


"""
Question 5: Given two lists, merge them into a single new list without modifying the originals.
"""


def list_merger(lst1, lst2):
    new_list = []
    for num in lst1:
        new_list.append(num)
    for num in lst2:
        new_list.append(num)
    return new_list


num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]


# Using + Operator
def merge_two_list(lst1, lst2):
    return lst1 + lst2


result = merge_two_list(num1, num2)
print("+ Method: ", result)


print(list_merger(num1, num2))


"""
Question 6: Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""


def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


nums = [1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]
print(remove_duplicates(nums))


"""
Question 7: Separate a list of integers into two distinct lists: one containing all the
even numbers and the other containing all the odd numbers.
"""


def even_odd_list(lst):
    even = []
    odd = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(f"Even: {even}")
    print(f"Odd: {odd}")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd_list(nums)


"""
Question 8: Create a list containing the squares of numbers from
1 to 10 (i.e., [1, 4, 9, ..., 100]).
"""
square_list = []

for num in nums:
    square = num**2
    square_list.append(square)

print(square_list)


"""
Question 9: Given a list of numbers (which may contain duplicates), write a Python script
that takes an integer as input from the user and removes all occurrences of that
integer from the list.
"""

# This is not a good approhc where you're looping or list and also try to remove things from it
# def target_remover(target, lst):
#     for num in lst:
#         if num == target:
#             lst.remove(num)
#     return lst


# # Reason is this here we supposed to get reuslt where 1 should be not in the list but it is
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]
# print(target_remover(1, nums))


# Better Approach
# def remove_occurance(target, lst):
#     result_list = []
#     for num in lst:
#         if num != target:
#             result_list.append(num)
#     return  result_list


# Reason is this here we supposed to get reuslt where 1 should be not in the list but it is
messy_list = [1, 1, 1, 1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1]
# print("New List")
# print(remove_occurance(1, messy_list))


# When we strcitly ordered to remove from the existing list
def remove_occurance(target, lst):
    while target in lst:
        lst.remove(target)
    return lst


print("Removed From Existing List")
print(remove_occurance(1, messy_list))


"""
Question 9: Write a Python script that iterates through a list of integers and replaces every
negative number found in the list with the value 0.
"""


def replace_negative(lst):
    lst_length = len(lst)
    for i in range(0, lst_length):
        if lst[i] < 0:
            lst[i] = 0
    return lst


nums = [1, 4, -1, -45, -100, 6, 7, 8, -1]
print(replace_negative(nums))


# Question 10: Create a list of squares of all odd numbers from 1 to 20. Using List Comprehension

odd_nums_square = [i * i for i in range(1, 21) if i % 2 != 0]
print(odd_nums_square)


"""
Question 11: Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""
# Note: List Comprehension is always use to create a new list
marks = [45, 87, 15, 94, 37, 89, 90, 99, 32, 11]
marks_greater_than_75 = [num for num in marks if num >= 75]
print(marks_greater_than_75)

print(marks, id(marks))
print(marks_greater_than_75, id(marks_greater_than_75))

print()

"""
Question 12: Given a 3x3 matrix as input, print its lower triangle.
Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

1  *  *
4  5  *
7  8  9
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


rows = len(matrix)
columns = len(matrix[0])

for outer in range(0, rows):
    for inner in range(0, columns):
        if outer >= inner:
            print(matrix[outer][inner], end=" ")
        else:
            print("*", end=" ")
    print()


print()
"""
Question 13: Given a 3x3 matrix, print its upper triangle.
Replace all elements in the lower triangle (below the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

Expected Output:
1  2  3
*  5  6
*  *  9
"""

for outer in range(0, rows):
    for inner in range(0, columns):
        if outer <= inner:
            print(matrix[outer][inner], end=" ")
        else:
            print("*", end=" ")
    print()

print()

"""
Question 14: Given a 3x3 matrix, print only the main diagonal elements and replace
everything else with an asterisk (*).
# 1 2 3
# 4 5 6
# 7 8 9

# Expected Output:
# 1 * *
# * 5 *
# * * 9

"""

for outer in range(0, rows):
    for inner in range(0, columns):
        if outer == inner:
            print(matrix[outer][inner], end=" ")
        else:
            print("*", end=" ")
    print()

print()

"""
Question 15: Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).

1  2 3
4  5 6
7  8 9

Expected Output:
*  * 3
*  5 *
7  * *
"""


for outer in range(0, rows):
    for inner in range(0, columns):
        if outer + inner == columns - 1:
            print(matrix[outer][inner], end=" ")
        else:
            print("*", end=" ")
    print()

print()

"""
Question 16: Given a 6x6 matrix, print only the border elements and replace the
inner elements with an asterisk (*).
"""

matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9],
]

rows = len(matrix)
columns = len(matrix)

for r in range(rows):
    for c in range(columns):
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
            print(matrix[r][c], end=" ")
        else:
            print("*", end=" ")
    print()
