"""
Question 1: Take a number as input. Print whether it is positive, negative, or zero.
"""

# num = int(input("Enter a number = "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

"""
Question 2: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

# num1 = int(input("Enter num1 = "))
# num2 = int(input("Enter num2 = "))

# if num1 > num2:
#     print(f"{num1} Greater then {num2}")
# elif num1 < num2:
#     print(f"{num1} Less then {num2}")
# else: 
#     print("Both are equal")

"""
Question 3:
Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""

# studentMarks = int(input("Enter your marks:"))
# if studentMarks >= 90 and studentMarks <= 100:
#     print("Your Grade: A")
# elif studentMarks >= 75 and studentMarks <= 89:
#     print("Your Grade: B")
# elif studentMarks >= 60 and studentMarks <= 74:
#     print("Your Grade: C")
# elif studentMarks >= 40 and studentMarks <= 59:
#     print("Your Grade: D")
# elif studentMarks >= 0 and studentMarks <= 40:
#     print("Your Grade: F")
# else:
#     print("Invalid marks")

"""
Question 4:
Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400.

200 - not a leap year
204 - leap

800 - leap year
"""
year = int(input("Enter Year: "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print ("Leap Year")
else: 
    print ("Not a Leap Year")