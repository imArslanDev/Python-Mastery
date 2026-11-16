# Make a new list from 1 to 10 -> [1,2,3,4...9,10]

# Traditional Way
new_list = []
for i in range(1, 11):
    new_list.append(i)
# print(new_list)

# By Using List Comprehension
list_one = [i for i in range(1, 11)]
list_two = [i + 10 for i in range(10, 0, -1)]

# print(list_one)
# print(list_two)

# 1 to 10, but all square
square_list = [i * i for i in range(1, 11)]
# print(square_list)

#  1 to 20, but only even numbers
even_list = [i for i in range(1, 21) if i % 2 == 0]
# print(even_list)

# Question: From 1 to 100, make a list of all prime numbers

def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


new_list = [i for i in range(1, 101) if is_prime(i)]
print(new_list)
