"""
Question: Ask a number from the user, and print all the factors.
"""

num = int(input("Enter a number: "))

# Solution:
i = 1

print(f"Factors of {num} are:", end=" ")
while(i <= num):
    if(num % i == 0):
        print(i, end=",")
    i += 1
