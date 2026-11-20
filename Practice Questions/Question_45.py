"""
Question: Write a lambda function that takes a number and returns "Positive", or 
"Negative".
"""

# Solution

positive_or_negative = lambda num: "Positive" if num >= 0 else "Nagative"

result = positive_or_negative(6)
print(result)