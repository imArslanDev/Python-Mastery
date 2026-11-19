"""
Question:  A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
"""

# Solution:

shopping_amount = float(int(input("Enter your shoping amount: ")))

if shopping_amount > 5000:
    discount_rate = 0.20
    label = "20%"
elif shopping_amount > 2000:
    discount_rate = 0.10
    label=  "10%"
elif shopping_amount > 1000:
    discount_rate = 0.05
    label = "5%"
else:
    discount_rate= 0.0
    label = "0%"

discount_amount = shopping_amount * discount_rate
final_amount = shopping_amount - discount_amount

if discount_rate > 0:
    print(f"You got a {label} discount. Total was {shopping_amount}, now pay: {final_amount:.2f}")
