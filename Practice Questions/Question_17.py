"""
Question: Sum of all the numbers from 1 to 100 divisible by 2 and 7
"""

# Solution:
i = 1
total = 0
while(i <= 100):
    if(i % 2 == 0 and i % 7 == 0):
        total += i
    i += 1

print(f"Sum of numbers from 1 to 100 divisible by 2 and 7 is: {total}")