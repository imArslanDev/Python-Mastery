"""
Question: Write a function tax_calculator(income) that takes annual income and returns 
the tax amount based on these slabs:
1- Up to 2,50,000 → No tax
2- 2,50,001 to 5,00,000 → 5%
3- 5,00,001 to 10,00,000 → 20%
4- Above 10,00,000 → 30%
"""

# Solution

def tax_calculator(income):
    if income <= 250000:
        tax_rate = 0
        label = "No Tax"
    elif income <= 500000:
        tax_rate = 5
        label = "5% Tax"
    elif income <= 1000000:
        tax_rate = 20
        label = "20% Tax"
    else:
        tax_rate = 30
        label = "30% Tax"

    tax_amount = income * tax_rate / 100
    return f"You have to pay {tax_amount:.2f} tax on your {income} income which is {label}"


print(tax_calculator(2000000))
