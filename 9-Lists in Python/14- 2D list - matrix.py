# 5x5
matrix = [
    [4, 8, 1, 2, 6],
    [9, 7, 2, 4, 8],
    [5, 6, 0, 1, 3],
    [45, 32, 1, 3, 2],
    [1, 2, 3, 4, 5],
]
total = 0

for i in range(0, 5):
    for j in range(0, 5):
        total += matrix[i][j]

print(f"Total: {total}")

# Print 2nd Rows 5th Element
print(matrix[1][4])

print(f"45 = {matrix[3][0]} ")