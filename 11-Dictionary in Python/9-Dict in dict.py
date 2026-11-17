students = {
    "101": {"name": "Ali", "age": 21, "city": "Lahore"},
    "102": {"name": "Asim", "age": 20, "city": "Karachi"},
    "103": {
        "name": "Abid",
        "age": 22,
        "city": "Multan",
        "details": {"ph": 123456789, "gender": "Male"},
    },
}

# How to access
print(students["101"])
print(students["102"]["age"])
print(students["103"]["details"]["ph"])


total = 0

for roll_no, details in students.items():
    print(f"Rol No: {roll_no} Student Name: {details["name"]} City: {details["city"]}")
    # In case asked to print the total age of all students
    total += details["age"]


print(total)