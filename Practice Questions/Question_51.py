"""
Question: Create a list of 6 hypothetical student marks (e.g., [75, 88, 62, 91, 70, 83]). Using built-in functions, print the highest mark, lowest mark, total sum of marks, and the average mark. 
Format the average to two decimal places
"""

# Solution

marks = [75, 88, 62, 91, 70, 83]

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)

print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Total Marks: {total}")
print(f"Average Mark: {average:.2f}")