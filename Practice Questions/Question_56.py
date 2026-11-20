"""
Question: Given two lists of the same length, write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
"""

# Solution

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print(result)  # [11, 22, 33, 44]