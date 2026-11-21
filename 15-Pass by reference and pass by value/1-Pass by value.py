def add_number(x):
    x = x + 1
    print(f"Parameter x addres: {id(x)}")
    print(f"Inside function: {x}")

    

num = 100

print(f"Variable Num address: {id(num)}")

add_number(num)
print(f"Outside function: {num}")



"""
Yahan `int` ek immutable object hai. Jab `add_number(num)` call hota hai,
to shuru mein parameter `num` aur bahar wala `num` dono ek hi `100` wale object
ko refer karte hain. Lekin chunkay `int` immutable hai, isliye function ke andar
`num = num + 1` karne par purana object badalta nahi balkay ek naya object (`101`)
ban jata hai aur parameter `num` us naye object ko point karne lagta hai.
Is wajah se outside wale `num` ki value `100` hi rehti hai aur increase nahi hoti.
"""