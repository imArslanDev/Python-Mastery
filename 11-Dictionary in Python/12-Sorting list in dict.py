marks = {
    "Ali": [43, 12, 98, 10, 22],
    "Zubair": [76, 55, 34, 89, 61],
    "Basit": [20, 45, 67, 30],
    "Mustakeem": [91, 73],
    "Faisal": [38, 82, 47, 95, 29],
}

# result = dict(sorted(marks.items(), key=lambda item: item[1][-1]))
result = dict(sorted(marks.items(), key=lambda item: sum(item[1])))
print(result)

for name, mark in marks.items():
    print(f"{name} Marks: {sum(mark)}")