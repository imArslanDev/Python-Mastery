marks = {
    "Science": 99,
    "Maths": 100,
    "Comp": 96,
    "Urdu": 80,
    "History": 71,
}

total = 0

for mark in marks.values():
    print(f"Marks: {mark}")
    total += mark

print(total)
