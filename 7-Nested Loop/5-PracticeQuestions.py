# Pattern 1:
"""
1
2 1 
3 2 1
4 3 2 1
5 4 3 2 1
"""
print("Pattern 1: ")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

# Pattern 2:
"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

print("Pattern 2: ")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

# Pattern 3:
"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
print("Pattern 3: ")
for i in  range(5, 0, -1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()

print()

# Pattern 4:
"""
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
"""

print("Pattern 4:")
for i in range(0, 6):
    for j in range(5, i, -1):
        print(j, end=" ")
    print()

# Pattern 5:
"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""

print("Pattern 5:")

for i in range(1, 6):
    # 1. Pehla inner loop: Spaces print karne ke liye
    for s in range(5 - i):
        print(" ", end=" ")
        
    # 2. Doosra inner loop: Numbers print karne ke liye
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
        
    print()

print()

# Pattern 6:

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


print("Pattern 6:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print()

# Pattern 7:

"""
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
"""

print("Pattern 7:")

for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

for i in range(2, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

print()

# Pattern 8:
print("Pattern 8:")

for i in range(1, 10, 1):
    for k in range(1, i):
        print(k, end=" ")
    print()