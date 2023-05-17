#import math
#
#print("Pythagorean Theorum Calculator")
#print("""
#
#  |\ 
#  | \ 
#  |  \  c
#a |   \ 
#  |    \ 
#  |_____\ 
#     b
#""")
#
#a = int(input("Leg a= "))
#b = int(input("Leg b = "))
#hypotenuse = int(input("Hypotenuse c = "))
#
#print((a*a)+(b*b))

import math

def pythagorean_theorem():
    known_side = input("Which side do you want to know (a, b, or c)?: ")
    
    if known_side.lower() == "a":
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of the hypotenuse: "))
        a = math.sqrt(c**2 - b**2)
        print(f"The length of side a is {a}")
    elif known_side.lower() == "b":
        a = float(input("Enter the length of side a: "))
        c = float(input("Enter the length of the hypotenuse: "))
        b = math.sqrt(c**2 - a**2)
        print(f"The length of side b is {b}")
    elif known_side.lower() == "c":
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = math.sqrt(a**2 + b**2)
        print(f"The length of the hypotenuse is {c}")
    else:
        print("Invalid input. Please enter 'a', 'b', or 'c'.")
        
pythagorean_theorem()
