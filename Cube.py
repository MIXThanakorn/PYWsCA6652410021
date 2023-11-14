import math
def calto_twodigits(x):
    return format(x,".2f")

def square_cube():
    print("+++++++++++++++++++")
    print("    Square cube")
    print("+++++++++++++++++++")
    def do_square_cube():
        try:
            W = float(input("Width of square: "))
            L = float(input("Lenght of square: "))
            H = float(input("Height of square: "))
            print(f"Square area is: {calto_twodigits(W*L*H)}")
        except ValueError:
            print("Please enter a number")
            do_square_cube()
    do_square_cube()

def circle_cube():
    print("+++++++++++++++++++")
    print("    Circle cube")
    print("+++++++++++++++++++")
    def do_circle_cube():
        try:
            R = float(input("Radius of circle: "))
            print(f"Circle area is: {calto_twodigits(4/3 * math.pi * R**3)}")
        except ValueError:
            print("Please enter a number")
            do_circle_cube()
    do_circle_cube()