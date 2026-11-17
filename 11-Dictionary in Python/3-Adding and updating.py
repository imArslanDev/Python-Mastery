user = {
    "name": "Arslan",
    "age": 21,
    "car":"Alsvin 1.5"
}

print(user, id(user))

# Update
user["age"] = 22

# Add
user["gender"] = "Male"

# Udate Multiple
user.update(
    {
        "city": "Lahore",
        "phone": 123456789,
        "age": 24,
        "car": "Alsvin 1.5 Lumiere",
    }
)

print(user, id(user))