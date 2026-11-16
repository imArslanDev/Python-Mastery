# Make a function which return min and max of a list

def min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return minimum, maximum

minValue, maxValue = min_max([10,20,40,60,100,-10])

print(f"Minimum Number is: {minValue}")
print(f"Maximum Number is: {maxValue}")