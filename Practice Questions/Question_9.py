"""
Q9: Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""
# Solution:

student_marks = int(input("Enter your marks:"))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif student_marks >= 90:
    print("Grade: A")
elif student_marks >= 75:
    print("Grade: B")
elif student_marks >= 60:
    print("Grade: C")
elif student_marks >= 40:
    print("Grade: B")
else:
    print("Grade: F")
