"""
In Python Dictionaries are = {}
1- Store data in key-value pairs
2- Unordered till python 3.7 but after Python preserves insertion order.
3- Mutable
4- Unique Keys Only if you try to create duplicate it simply overwrite the prev one
5- Keys are Immutable you can change the value but you can't change the key once you created

"""

marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    55: 100,
    101: "Asim",
    "abc": [1, 2, 3, 4],
    (11, 12): "Surat",
    "comp": 100,
}

print(marks)
print(type(marks))
print(marks.get("comp"))