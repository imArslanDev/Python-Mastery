# Pattern 1:
"""
        1
      1 2
    1 2 3    
  1 2 3 4
1 2 3 4 5
"""
print("Space Pattern 1: ")
for i in range(1, 6):
    for j in range(1, 6 - i):
        print( " ", end=" ")

    for k in range(1, i+1):
        print(k, end=" ")
    print()

print()

# Pattern 2:

"""
        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1  
"""
print("Space Pattern 2: ")

for i in range(5, 0, -1):
    
    for j in range(1, i):
        print( " ", end=" ")

    for k in range(5, i-1, -1):
        print(k, end=" ")
    print()