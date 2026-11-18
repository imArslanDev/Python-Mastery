text = "Arsal is a good developer and is learning python"
# python learning is and developer good a is Arsal

words = text.split()
reverse_list = words[::-1]
list_to_str = (" ".join(reverse_list))
print(list_to_str)