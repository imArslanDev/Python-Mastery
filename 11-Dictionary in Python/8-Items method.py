marks = {
    "Science": 99,
    "Maths": 100,
    "Comp": 96,
    "Urdu": 80,
    "History": 71,
}
# It gives me Tuples
# for dets in marks.items():
#     print(dets)

print(marks.items())

for details in marks.items():
    subject = details[0]
    mark = details[1]
    print(f"{subject} Marks: {mark}")

# Better Way Unpack the Tuple and use it
for subject, mark in marks.items():
    print(f"Subject: {subject} & Marks: {mark}")
