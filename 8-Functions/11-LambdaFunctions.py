# lambda functions are anonymous functions jin ke name nhi hote 

def find_square(num):
    return num ** 2

print(find_square(4))

addition = lambda num1, num2: num1 + num2
subtraction = lambda num1, num2:  num1 - num2 if (num1 >= num2) else "Num 1 must be a bigger number then Num2 for Subtraction"

print(addition(10, 20))
print(addition(5000, 120000))
print(subtraction(50, 10))
print(subtraction(20, 40))



# Return True if age>=18 else false
def is_adult(age):
    if age >= 18:
        return True
    return False


is_adult = lambda age: True if age >= 18 else False
print(is_adult(18))
print(is_adult(11))


