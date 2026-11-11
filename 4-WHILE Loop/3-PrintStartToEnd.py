# Taks: Print Start to End using While Loop

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

# Bad Approch Becuase Input Change ho rha ha
# while start <= end:
#     print(start, end= " ")
#     start += 1

# Good Approach
i = start
while i <= end:
    print(i, end=", ")
    i += 1

print(f"Start value after loop: {start}")
