import copy

def add_item(lst):
    print(f"Paramter lst address: {id(lst)}")
    lst.append("Good")
    print(f"Inside function: {lst}")


fruit_list = ["Apple", "Mango"]

print(f"Variable fruit_list address: {id(fruit_list)}")


add_item(fruit_list)
print(f"Outside function: {fruit_list}")

# Pass by reference
# reference = address

"""
Now here function jo lst le rha ha wo 1 mutable object hai.
Iska matlab yeh hai ke function mein jo list pass ki gayi hai, uska reference
aur function parameter (fruit_list) ka reference same hai. Is wajah se agar function
ke bahar `fruit_list` ko check karein, to usmein bhi `"Good"` append hua milega.
"""

# Solution
"""
If you want ke aesa na ho to use kro deep copy ko
"""

def add_item(lst):
    lst = copy.deepcopy(lst)
    lst.append("Good")
    print(f"Inside: {lst}")

fruit_list = ["Apple", "Mango"]
add_item(fruit_list)
print(f"Outside: {fruit_list}")
# Now Outside the function sirf wohi values ho gi jo bahir apne add ki ha "Apple" and "Mango"