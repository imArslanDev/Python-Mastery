"""
Question: Take the user's age as input. Check and Print whether they are eligible to vote (age >= 18) and whether they are a
Seior citizen (age >= 60) 
"""

# Solution:

user_age = int(input("Enter your age:"))

eligible_to_vote = user_age >= 18
senior_citizen = user_age >= 60

print(f"User age is: {user_age}.\nEligible For Vote ? : {eligible_to_vote}.\nIs Senior Citizen: {senior_citizen} ")