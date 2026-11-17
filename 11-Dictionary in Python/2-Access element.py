marks = {
    "Science": 99,
    "Maths": 100,
    "Comp": 96,
    "Urdu": 80,
    "History": 71,
}

# Access Elements form Dictionary
# print(marks["Urdu"])
# Here we can provde 2 thing key name and default value in case that is not available
# print(marks.get("English", "Not Available"))

subject = "Eng"
ans = marks.get(subject)

if ans is None:
    print("Subject not exist")
else:
    print(ans)
    