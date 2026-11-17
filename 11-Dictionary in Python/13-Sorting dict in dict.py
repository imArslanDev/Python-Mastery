students = {
    "Ali": {"math": 87, "science": 92, "english": 74},
    "Zubair": {"math": 65, "science": 78, "english": 90},
    "Basit": {"math": 55, "science": 60, "english": 48},
    "Mustakeem": {"math": 95, "science": 88, "english": 82},
    "Faisal": {"math": 70, "science": 45, "english": 63},
}

# Ascending Order ma Sort krega based on science marks low to high
ans = dict(sorted(students.items(), key=lambda x: x[1]["science"]))

# Descending Order ma Sort krega based on science marks high to low
ans = dict(sorted(students.items(), key=lambda x: x[1]["science"], reverse=True))

# Now list based on total scored marks low to high
ans = dict(
    sorted(
        students.items(), key=lambda x: x[1]["math"] + x[1]["science"] + x[1]["english"]
    )
)

# Better Way 
ans = dict(sorted(students.items(), key=lambda x: sum(x[1].values()), reverse=True))
print(ans)
