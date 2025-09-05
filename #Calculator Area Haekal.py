# Calculator Area
import math
print("================================================")
print("                Area Calculator                 ")
print("================================================\n")
print(" 1. Triangle\n 2. Square \n 3. Rectangle \n 4. Circle \n 5. Quit")

# Formula
area = int(input("Which Shape ? "))

# Logic

if area == 1:
    base = int(input("How much is cm of the Base? "))
    height = int(input("How much is cm of the Height? "))
    triangle = (base * height)/2
    print(triangle)
elif area == 2:
    base = int(input("How much is cm of the Base? "))
    square = base ** 2
    print(square)
elif area == 3:
    base = int(input("How much is cm of the Base? "))
    height = int(input("How much is cm of the Height? "))
    rectangle = base * height
    print(rectangle)
elif area == 4:
    radius = int(input("How much is cm of the radius? "))
    circle = math.pi * radius ** 2
    print(circle)
else:
    print("Invalid, Quiting Calculator....")

