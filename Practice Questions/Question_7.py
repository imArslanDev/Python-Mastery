# Question: Take a number as input. Print whether it is positive, negative, or zero

# Solution:
num = int(input("Enter a number:"))

if(num > 0):
    print(f"{num} is Positive")
elif(num < 0):
    print(f"{num} is Negitive")
else:
    print(f"{num} Zero")