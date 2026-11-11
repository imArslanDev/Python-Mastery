# # 1 to 10
# # i=5  loop stop

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1
#     if i == 5:
#         break


for init in range (1, 10, 1):
    if init == 5:
        break
    print(init)
