"""
✓ Must start with a letter or underscore (_)
✓ Can contain letters, digits, and underscores
✗ Cannot start with a digit
✗ Cannot use Python keywords (if, for, while...)
✓ Names are case-sensitive → age ≠ Age ≠ AGE
"""
age=5
Age=10
AGE=111
print(age,Age,AGE)

# Valid But not used in prjects
_ = 10
__ = 20
print(_ + __)

# Invalid 
# 1Age = "10" 