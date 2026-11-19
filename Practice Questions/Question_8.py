"""
Question: Take two numbers as input. Print the greater of the two. If they are 
equal, print "Both are equal.
"""
# Solution:

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))


if(num1 > num2):
    print(f"{num1} is greater.")
elif(num2 > num1) :
    print(f"{num2} is greater.")
elif(num1 == num2):
    print("Both are equal")