count = 0


def increase():
    global count
    count += 1
    print(f"Inside function count={count}")


increase() # 1
increase() # 2
increase() # 3
print(f"Outside function count={count}") # 3