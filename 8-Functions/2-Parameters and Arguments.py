# Take 3 int as a parameter and print total
def addition(a, b, c):
    sum = a + b + c
    print(f"Total: {sum}")

addition(12, 34, 42)

# Ask a  name age , gender, print
def greet(name, age, gender):
    print(f"Hey {name}! Your age is {age} and gender is {gender}")


name = input("Enter name = ")
age = int(input("Enter age = "))
gender = input("Enter gender = ")
greet(name, age, gender)
