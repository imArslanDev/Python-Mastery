"""
String Methods: Splitting and Joining
split(): Break String into List
join(): Combine List into String
"""

text = "Khan is a Developer"

# print(len(text.split()))

my_list = ["A", "r", "s", "a", "l", 5, 31.99, "python", "coder"]
ans = "-".join(str(ch) for ch in my_list)
print(ans)
print(type(ans))
