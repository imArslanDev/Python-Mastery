marks = [45, 34, 54, 65, 23, 65, 76, 91, 47]

# To get the length
length = len(marks)
print(f"Length of Marks list = {length}")

# Get Max Value
maximinmMarks = max(marks)
print(f"Maximum marks = {maximinmMarks}")

# Get Min Value
minimumMarks = min(marks)
print(f"Minimum marks = {minimumMarks}")

# Sum Total
total = sum(marks)
print(f"Total marks = {total}")

# To sort using sorted(), it will always return you a new list
new_list = sorted(marks, reverse=False)
print(f"New List = {new_list}")
print(f"Marks = {marks}")

# Check to verify
print(marks == new_list)  # False That means both are diffrent in memory
