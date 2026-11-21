def rebind(lst):
    lst = [100, 200, 500]
    print(f"Inside function: {lst}")

lst = [1,2,5]
rebind(lst)
print(f"Outside function: {lst} ")

"""
Rebinding ka matlab hai kisi variable (ya parameter) ko kisi purane object se
hatakar kisi naye object ke saath jod dena.

Yahan shuru mein bahar wala `lst` aur function parameter `lst` dono `[1, 2, 5]`
ko point kar rahe thay. Lekin jab function ke andar `lst = [100, 200, 500]` likha
gaya, to yeh purani list ko modify nahi kar raha balkay parameter `lst` ko ek
bilkul nayi list `[100, 200, 500]` par rebind (reassign) kar raha hai.
Is wajah se bahar wale `lst` par koi asar nahi parta aur woh `[1, 2, 5]` hi rehta hai.
"""