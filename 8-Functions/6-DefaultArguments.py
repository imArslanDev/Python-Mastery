# Default Arguments Hamesha Right Side Pr Hone Chaihia wrna Error ayega
def calculate_marks(maths, eng, urdu, computer=0, physics=0,):
    
    print(f"Maths = {maths}")
    print(f"Eng = {eng}")
    print(f"Urdu = {urdu}")
    print(f"Computer = {computer}")
    print(f"Physics = {physics}")
    total_marks = maths + eng + urdu + computer + physics
    print(f"Total marks scored = {total_marks}")

calculate_marks(100, 95, 90, 74, 73)
# TypeError: calculate_marks() missing 3 required positional arguments: 'maths', 'eng', and 'urdu'