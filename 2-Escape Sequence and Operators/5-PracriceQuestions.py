"""
Question 1: Take two numbers from user. Print their sum, difference, product and reminder
"""

input1 = int(input("Enter First Number:"))
input2 = int(input("Enter Second Number:"))

print(f"Sum: {input1 + input2}")
print(f"Difference: {input1 - input2}")
print(f"Product: {input1 * input2}")
print(f"Reminder: {input1 % input2}")

"""
Question 2: Take a number from user. Print their it is Even or Odd
"""

isEven = input1 % 2 == 0
isOdd = not (input1 % 2 == 0)
print(f"Number: {input1} Even: {isEven}" )
print(f"Number: {input1} Odd: {isOdd}" )

"""
Question 3: Take user's age as input. Check and print whether they are eligible to vote and whether they are senior citizens
"""
userAge = int(input("Enter your age:"))
isEligibleForVote = userAge >= 18
isSeniorCitizen = userAge >= 60

print(f"User age is: {userAge}. Eligible For Vote ? : {isEligibleForVote}. Is Senior Citizen: {isSeniorCitizen} ")

"""
Question 4: A Student scored marks in 3 Subjects. Take all thre as input,
calculate the total and average and Print both using f-string.
"""
subj1Marks = 66
subj2Marks = 75
subj3Marks = 89

total = subj1Marks + subj2Marks + subj3Marks
avg = total / 3

print(f"Total scored: {total} Marks \nAverage: {avg:.2f} ") # avg:.2f Shows upto 2 decimals tak output dikhao