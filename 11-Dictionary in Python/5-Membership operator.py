student = {
    "name": "Hadi",
    "age": 25,
    "gender": "Male",
    "city": "Surat",
}

k = input("Enter key = ")

if k in student:
    print(student[k])
else:
    print("Key does not exist")
