import math
def calto_twodigits(x):
    return format(x,".2f")

def square_area():
    print("+++++++++++++++++++")
    print("    Square area")
    print("+++++++++++++++++++")
    def do_square_area():
        try:
            W = float(input("Width of square: "))
            L = float(input("Lenght of square: "))
            print(f"Square area is: {calto_twodigits(W*L)}")
        except ValueError:
            print("Please enter a number")
            do_square_area()
    do_square_area()

def circle_area():
    print("+++++++++++++++++++")
    print("    Circle area")
    print("+++++++++++++++++++")
    def do_circle_area():
        try:
            R = float(input("Radius of circle: "))
            print(f"Circle area is: {calto_twodigits(math.pi * R **2)}")
        except ValueError:
            print("Please enter a number")
            do_circle_area()
    do_circle_area()