# Question 1: Write a function to ask a number from user and prints if that number is even or odd

def check_number(num):
    if(num % 2 == 0):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# num = int(input("Enter a number: "))
# check_number(num)


# Question 2: Write a function that print all the factors of a number entered by user
def print_factors(num):
    print(f"Factors of {num} are:", end=" ")
    for i in range(1, num + 1):
        if(num % i == 0 ):
            print(i, end=" ")
    print()

# num = int(input("Enter a number: "))

# print_factors(num)



"""
Question 3: Write a function called add that takes two numbers as parameters
and prints their sum.
"""


def add(num1, num2):
    print(f"Sum: {num1 + num2}")
add(20, 100)

"""
Question 4: Write a function called rectangle_area that takes length and breadth
as parameters and prints the area.
"""

def rectangle_area(length, breadth):
    area = length * breadth
    print(f"Area of rectangle is: {area}")

rectangle_area(10, 20)
rectangle_area(4, 2)


"""
Question 5: Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""

def find_max(num1, num2, num3):
    largest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
    print(f"Largest Number is: {largest}")

find_max(1, 0, 20)

"""
Question 6: Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""

def discount_price(original_price, discount_percent):
    discount_amount = (discount_percent / 100)  * original_price
    final_amount = original_price - discount_amount
    print(f"Oringal Price:{original_price}")
    print(f"Price you have to pay after discount:{final_amount}")

discount_price(250, 10)


"""
Question 7: Write a function called square that takes a number and returns its square.
Store the result and print it.
"""

def square(num):
    res = num ** 2
    return f"Square of {num} is: {res}"
print(square(4))


"""
Question 8: Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""

def min_of_three(num1, num2, num3):
    smallest = num1 if (num1 <= num2 and num1 <= num3) else (num2 if num2 <= num3 else num3)
    return smallest
print(min_of_three(10, 20, -100))


"""
Question 9: Write a function called absolute_value that takes a number and returns
its absolute value without using the built-in abs() function.
"""
def absolute_value(num):
    return num if num >= 0 else -num

print(absolute_value(15))
