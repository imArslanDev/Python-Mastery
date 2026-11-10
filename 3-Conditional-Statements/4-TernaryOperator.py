age = int(input("Enter age = "))

# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"
status = "Adult" if age >= 18 else "Minor"

print(f"Your status is {status}")

output = "You're eligible to vote" if age >= 18 else "Not eligible to vote"
print(output)