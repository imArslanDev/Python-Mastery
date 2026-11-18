"""
Question: A student scored marks in 3 subjects. Take all three as input, calculate the total and average,
And print both using an f-string.
"""

# Solution:
marks_in_urdu = int(input("Enter your Urdu marks:"))
marks_in_maths = int(input("Enter your Maths marks:"))
marks_in_english = int(input("Enter your English marks:"))

total_marks_scored = marks_in_urdu + marks_in_english + marks_in_maths
average_marks = total_marks_scored/3

print(f"Your Scored Total {total_marks_scored} marks.\nAverage: {round(average_marks)}")