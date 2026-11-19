"""
Question: Print This Pattern
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""

# Solution

for i in range(1, 6):
    print("  " * (5 - i), end="")
    for j in range(1, 2 * i):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    print("  " * (5 - i), end="")
    for j in range(1, 2 * i):
        print("*", end=" ")
    print()