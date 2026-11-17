marks = {"math": 85, "science": 92, "english": 90, "urdu": 78}

ans = dict(sorted(marks.items(), key=lambda x: x))
print(ans)

"""
Step-by-Step Explanation
Step 1: marks.items()
Kya karta hai: Yeh dictionary ke har ek key-value pair ko ek tuple ((key, value)) mein badal kar ek list de deta hai.

Example:[('math', 85), ('science', 92), ('english', 90), ('urdu', 78)]

Step 2: sorted(..., key=lambda x: x)
Kya karta hai: Yeh us list ko sort karta hai.

key=lambda x: x ka matlab: Yeh function har tuple (x) ko waise ka waisa hi return karta hai. Python mein jab tuples ko sort kiya jata hai, toh woh pehle element (key, yani subject ka naam jaise "math", "science") ke hisab se alphabetical order mein sort karta hai.

Note: Kyunki yeh default behavior bhi hai, isme key=lambda x: x na bhi likhein tab bhi code wahi kaam karega!

Step 3: dict(...)
Kya karta hai: sorted() function humesha ek list return karta hai (tuples ki). Isliye dict() function ka use karke hum us sorted list ko wapas se ek dictionary mein convert kar dete hain.

Step 4: print(ans)
Kya karta hai: Final sorted dictionary ko screen par print kar deta hai.

Final Output
Jab aap is code ko run karenge, toh output yeh aayega:
"""

# Convert list or tuple into dictionary
result = sorted(marks.items(), key=lambda item: item)
converted = dict(result)
print(type(converted), converted)