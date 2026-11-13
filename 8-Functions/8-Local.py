# Local Variable
def addition(n1, n2, n3):
    total = n1 + n2 + n3
    print(f"Total = {total}")


addition(10, 20, 30)

def xyz(n1, n2):
    n1 = 100 # Local Variable
    n2=  200 # Local Variable
    print(f"Inside function n1={n1} and n2={n2}")

a = 50 # Global Variable
b = 80 # Global Variable

xyz(a, b) # 100, 200
print(a) # 50
print(b) # 80