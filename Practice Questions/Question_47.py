"""
Question: Write a function power(base, exp) that returns base raised to exp using a 
loop - no ** operator or pow() allowed.
"""

# Solution

def power(base, exp):
    result = 1
    
    for i in range(exp):
        result *= base
    return result

res = power(5, 2)
print(res)