"""
Question: Given a list of numbers, use a loop to calculate and print their average. You can use len() to get the count of elements, but avoid using sum() for the total. 
Format the average to two decimal places.
"""

# Solution

scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"The average score is: {average:.2f}")