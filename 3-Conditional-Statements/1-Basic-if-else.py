age = int(input("Enter your age = "))

if age >= 18:
    print("You can vote")
    print("You are eligible")
    print("You are responsible voter")
else: 
    print("You cannot Vote")

engMarks = int(input("Enter your English marks = "))
mathMark = int(input("Enter your Math marks = "))

passingMarks = 33
if engMarks > passingMarks and mathMark > passingMarks:
    print("Pass")
else:
    print("Fail")