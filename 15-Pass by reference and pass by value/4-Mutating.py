def mutating(lst):
    lst.append(100)
    print(f"Inside function: {lst}")

lst = [1,2,5]

mutating(lst)
print(f"Outside function: {lst} ")

"""
Isay mutating kehte hain — jab aap kisi object ko poora change (replace)
nahi kar rahe hotay, balkay uske andar wali cheezon ko modify kar rahe hotay hain.

Yahan bahar wale `lst` aur function parameter `lst` dono ek hi list object
`[1, 2, 5]` ko point kar rahe hain. `.append(100)` ussi list ke andar `100`
add kar deta hai, isliye outside function bhi `lst` `[1, 2, 5, 100]` ho jata hai.
"""