# Q-1: Print all the numbers which are divisible by 3 and 5 from 1 to 100.
# start = int(input("Start Number: "))
# end = int(input("End Number: "))

# i = start

# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=" ")
#     i += 1
    
# Q-2: Sum of all the numbers from 1 to 100.

# i = start
# total = 0
# while i <= end:
#     total = total + i
#     i += 1
# print(f"Total: {total}")

# Q-3: Sum of all the numbers from 1 to 100 divisible by 2 and 7.

# i = start
# total = 0
# while i <= end:
#     if i % 2 == 0 and i % 7 == 0:
#         print(f"Numbers Dvisible by 2 and 7: {i}")
#         total = total + i
#     i += 1
# print(f"Total: {total}")


# Q-4: Ask a number from the user print the multiplication table upto 10.
# i = 1

# num = int(input("Enter a number: "))

# while i <= 10:
#     print(f"{num} x {i} = {i * num }")
#     i += 1

# Q-5: Ask a number from the user and print all the factors. 
i=1
num = int(input("Enter a number: "))
while i <= num:
    if(num % i == 0):
        print(i, end=" ") 
    i += 1