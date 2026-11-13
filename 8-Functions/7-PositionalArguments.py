# Positional / Keyword Arguments
 
def calculate_marks(maths, eng, urdu, computer=0, physics=0,):   
    print(f"Maths = {maths}")
    print(f"Eng = {eng}")
    print(f"Urdu = {urdu}")
    print(f"Computer = {computer}")
    print(f"Physics = {physics}")
    total_marks = maths + eng + urdu + computer + physics
    print(f"Total marks scored = {total_marks}")

# Norfmally Jis Order Ma Parameter leta ha usi order ma Argument bhi pass krte ha but 
# If you not want to follow the order you can assign the value this way randomly
calculate_marks(physics=90, eng=98, computer=100, maths=100, urdu=99)
