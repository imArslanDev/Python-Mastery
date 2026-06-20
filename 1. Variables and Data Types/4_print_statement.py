# 3 Diffrent Ways of Print()

name="Arslan"
age=20
gender='Male'

# 1- Simple Print() function 
print("Hello",name, "your age is", age, "and gender is", gender)
# print("Hello " + name + " your age is " + age + " and gender is " + gender) # Err
# print("Hello " + name + " your age is " ,age, " and gender is " + gender) # Correct

# Multiline Comment Example
"""
This is a
Multiline
Comment

"""

# 2- Print using sep or end
print(name, age, gender, sep="-")
# By Default Print Statement takes Single line to end.
print(name,end="-120-") # End on same line with -120-
print(age,end=" ") # End on same line with space
print(gender)

# 3- Print using F-String
print(f"Your name is {name}, age is {age+1} and gender is {gender}")
print(age)