"""
Question 1: Email Validation

Take an email as input. Validate that it contains exactly one @ and at least
one .
Print "Valid" or "Invalid".
"""


def check_email(email: str):
    if email.count("@") == 1 and "." in email:
        return "Valid"
    return "Invalid"


email = "imArslan7061@gmail.com"
print(check_email(email))

"""
Question 2: Clean Phone Number

Take a phone number as input in the format +92 312-456-7890. Remove all dashes
and the country code. Print the cleaned 10-digit number.
"""


def clean_number(phone_number: str):
    phone_number = phone_number.replace("-", "")
    phone_number = phone_number.replace("+92", "")
    print(phone_number)


phone = "+92 3124567890"
clean_number(phone)

"""
Question 3: Vowel-Starting Words

Take a sentence as input. Split it into words and print how many words start
with a vowel.
"""


def count_vowel_words(sentence: str):
    vowels = "aeiouAEIOU"
    count = 0
    words = sentence.split()
    for word in words:
        if word[0] in vowels:
            count += 1
    return count


sentence = "Arslan is an excellent coder and a great engineer"
print(count_vowel_words(sentence))

"""
Question 4: Sorted Names

Take a list of names as input (comma separated). Split them, sort them
alphabetically, and join them back with " | " as separator.
"""

names_input = "Charlie,Alice,Ethan,Bob,Diana"
words = names_input.split(",")
print(" | ".join(words))


"""
Question 5: File Type Check

Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx,
or .txt and print the file type.
"""

filename = "report.mp3"
if filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".txt"):
    print("Valid file")
else:
    print("Invalid file")

"""
Question 6: Longest Word

Take a sentence as input. Print the longest word in it.
"""


def print_longest_word(sentence: str):
    words = sentence.split()
    print(max(words, key=lambda x: len(x)))
    # longest_count = 0
    # longest_word = ""
    # for word in words:
    #     if len(word) > longest_count:
    #         longest_count = len(word)
    #         longest_word = word
    # print(longest_word)


sentence = "Arslan is learning Python programming every single day"
print_longest_word(sentence)


"""
Question 7: Username Validation

Take a username as input. Strip any spaces from both sides and check if the
cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".
"""


def validate_username(username: str):
    username = username.strip()
    if username[0].isdigit():
        return "Invalid"
    return "Valid"


username = "  1Arslan123"
print(validate_username(username))

"""
Question 8: Unique Words Count

Take a paragraph as input. Print the count of unique words in it
(case insensitive).
"""


def count_unique_words(paragraph: str):
    words = paragraph.split()
    return len(set(words))


paragraph = "Python is great and Python is fun and learning Python is the best"
print(count_unique_words(paragraph))

"""
Question 9: Palindrome Check

Write a function is_palindrome(text) that returns True if the given string is
a palindrome (ignoring case and spaces).
"""


def is_palindrome(text: str):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("Never odd or even"))
print(is_palindrome("hello"))


"""
Question 10: Word Lengths (Homework)

Take a sentence as input. Print each word's length next to it.
Example: Python (6) is (2) great (5).
"""

sentence = "Arslan is learning Python programming every single day"


"""
Question 11: Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in
each word). Example: "Python is fun" -> "fun is Python".
"""


def reverse_words(sentence: str):
    words = sentence.split()
    words = words[::-1]
    return " ".join(words)


sentence = "Arslan is learning Python programming every single day"
print(reverse_words(sentence))


# Palindrome: Aesa string jisko seedha prho ya ulta output same ata ha e.g: Civic, Level, M dam