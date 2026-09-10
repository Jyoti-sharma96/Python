import math

def calculate_factorial():
    try:
        n = int(input("Enter a number: "))
        print(f"Factorial: {math.factorial(n)}")
    except ValueError:
        print("Invalid input.")

def calculate_compound_interest():
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))
        amount = p * (pow((1 + r / 100), t))
        ci = amount - p
        print(f"Compound Interest: {ci:.2f}")
    except ValueError:
        print("Invalid input.")

def trigonometric_calculations():
    try:
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print(f"Sin: {math.sin(rad):.2f}, Cos: {math.cos(rad):.2f}, Tan: {math.tan(rad):.2f}")
    except ValueError:
        print("Invalid input.")

def area_geometric_shapes():
    shape_choice = input("1. Circle\n2. Rectangle\nEnter choice: ")
    if shape_choice == '1':
        r = float(input("Enter radius: "))
        print(f"Area: {math.pi * (r ** 2):.2f}")
    elif shape_choice == '2':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Area: {l * w:.2f}")