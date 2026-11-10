#Explicit Conversion
num1 = "100"
num2 = "200"

num1Converted = int(num1)
num2Converted = int(num2)

print(num1Converted + num2Converted)

print("Wrong:", int(num1 + num2))
print("Correct:", int(num1) + int(num2))

# Type Before Conversion
print(num1, type(num1))
print(num2, type(num2))

# Type After Conversion
print(num1Converted, type(num1Converted))
print(num2Converted, type(num2Converted))

# mixNum = "120ABC"
# print(int(mixNum)) # Err

a = 700.5
print(int(a))