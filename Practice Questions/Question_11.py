"""
Question: Take a person's age and whether they have a valid ID (True/False) as input. They 
can enter a venue only if they are 18 or older AND have a valid ID. Print the 
appropriate message.
"""

# Solution:

age = int(input("Enter your age: "))
valid_id = input("Do you have valid ID? (True/False): ").strip().lower()

if(age >= 18 and valid_id) :
    print("Welcome to our venue")
else:
    print("You must be 18 and have valid id to enter the venue")
