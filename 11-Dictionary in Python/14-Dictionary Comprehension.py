sqaures = {}

for i in range(1, 11):
    sqaures[i] = i * i

print(sqaures)

# Dictionary Comprehension Same Result in one line
sqaures = {i: i * i for i in range(1, 11)}
print(sqaures)


# With a condition
marks = {"math": 87, "science": 92, "english": 74, "urdu": 80}

# Show only those subjects where marks > 80
filterTopSubject = {subject: mark for subject, mark in marks.items() if mark > 80}
print(filterTopSubject)

# Transform double all marks
doubled = {subject: mark * 2 for subject, mark in marks.items()}
print(doubled)

# Creating a dict from two lists
subjects = ["math", "science", "english", "urdu"]
marks = [87, 92, 74, 80]

"""
zip is a built-in function in python that pairs elements from multiple iterables (such as lists, tuples, or strings) into a single iterator of tuples.
"""
result = {subject: mark for subject, mark in zip(subjects, marks)}
print(result)