"""
Question 1: Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values() to
calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Science": 99,
    "Maths": 100,
    "Comp": 96,
    "Urdu": 80,
    "History": 71,
}

total_subjects = len(marks)
total_marks = 0
for mark in marks.values():
    total_marks += mark
    

print(f"Total Marks = {total_marks}")
print(f"Average Marks Obtained = {total_marks/total_subjects}")

"""
Question 2: Top Scorers

Populate a dictionary with six student names and their corresponding marks.
Loop through it and print the names of all students who achieved a score above 75.
"""

students = {
    "Alice": 82,
    "Bob": 67,
    "Charlie": 91,
    "Diana": 74,
    "Eve": 88,
    "Frank": 55,
}

for name, mark in students.items():
    if mark >= 75:
        print(f"{name} Scored {mark} Marks")


"""
Question 3: Dictionary Merge Function

Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries
(d1 and d2) as arguments and returns a new dictionary formed by merging them
using the update() method. Ensure d1 remains unchanged.
"""


def  merge_dicts(d1, d2):
    new_dictionary = {}
    new_dictionary.update(d1)
    new_dictionary.update(d2)
    return new_dictionary

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}

ans = merge_dicts(d1, d2)
print(ans)