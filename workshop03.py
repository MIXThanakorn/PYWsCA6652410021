import math
import area
import Cube

def calto_twodigits(x):
    return format(x,".2f")

def Sign_out():
    print("Signing out")
    exit

print("+++++++++++++++++++")
print("   Area and Cube")
print("+++++++++++++++++++")

print("""
      1. Square Area
      2. Circle Area
      3. Square Cube
      4. Circle Cube
      0. Sign out
      """)

def Choose_Menu():
    print("+++++++++++++++++++++++++++++++++")
    Menu = input("Choose menu: ")
    if Menu == "0":
        Sign_out()
    elif Menu == "1":
        area.square_area()
        Choose_Menu()
    elif Menu == "2":
        area.circle_area()
        Choose_Menu()
    elif Menu == "3":
        Cube.square_cube()
        Choose_Menu()
    elif Menu == "4":
        Cube.circle_cube()
        Choose_Menu()
    else:
        print("Please choose menu for list")
        print("+++++++++++++++++++++++++++++++++")
        Choose_Menu()

Choose_Menu()