"""
Question:  Write a function called discount_price that takes original_price 
and discount_percent as parameters and prints the final price after discount
"""

# Solution

def discount_price(original_price, discount_percent):
    discount_price = original_price * discount_percent / 100
    final_price = original_price - discount_price
    print(f"Final Price after discount: {final_price:.2f}")


discount_price(250, 5)