"""
Q10: Take a year as input. Check if it is a leap year. A year is a leap 
year if it is divisible by 4, but not by 100, unless it is also 
divisible by 400.
"""

# Solution:

year = int(input("Enter an year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")