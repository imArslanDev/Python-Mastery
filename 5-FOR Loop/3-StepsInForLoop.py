# Steps in for loops

# - 10 sa Positive 3 tak ki range ha
# for i in range(-10, 4, 1 ):
#     print(i, end=", ")

#  -100 sa Positive 100 ka sare numbers print krega jo 5 sa divisible honge
for i in range(-100, 105, 1):
    if i % 5 == 0:
        print(i, end=" ")