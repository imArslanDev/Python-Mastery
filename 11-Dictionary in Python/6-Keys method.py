marks = {
    "Science": 99,
    "Maths": 100,
    "Comp": 96,
    "Urdu": 80,
    "History": 71,
}

total = 0

for subject in marks.keys():
    print(f"Subject: {subject} Marks: {marks[subject]} ")
    total += marks[subject]

print(total)