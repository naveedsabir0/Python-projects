from math import pi


def trapezoid():
    b1 = float (input ("Please enter the size of the large base: "))
    b2 = float (input ("Please enter the size of the small base: "))
    h = float ( input( "Enter the height (h): "))
    surface = ((b1+b2)/2)*h
    print("The total surface of the trapezoid is:", surface)
    return 

def parallelogram():
    
    b = float (input ("Please enter the base size: "))
    h = float ( input( "Enter the height (h): "))
    surface = b*h 

    print("The total surface of the parallelogram is:", surface)
    return 

def rectangle():
    b = float (input ("Please enter the base size:"))
    h = float ( input( "Enter the height (h): "))
    surface = b*h 

    print("The total surface of the rectangle is:", surface)
    return 

def square():
    s = float (input("Enter the side size: "))
    surface  = s * s
    print("The total surface of the square is:", surface)
    return

def triangle():
    b = float (input ("Please enter the base size: "))
    h = float ( input( "Enter the height (h): "))
    surface = (b*h)/2

    print("The total surface of the triangle is:", surface)
    return 
    
def circle():
    r = float(input("Enter the radius of the circle: "))
    surface = pi * (r*r)
    print ("The total surface of the circle is:", surface)
    return

# main program
print ("""This program will calculate the surface of the different shapes
The user must enter the mesurements of the shapes. All the size should be in cm or metres.
But it can also work with other units.

First the user will be asked to choose a shape and then he will have to enter the size of all the required sides.
""")
print()

choice = input("""       WELCOME!!!

1. Trapezoid
2. Parallelogram
3. Rectangle
4. Square
5. Triangle
6. Circle
7. Exit

Enter your choice: 
""")

while choice not in ["1","2","3","4","5","6","7"]:
    choice = input("ERROR! Wrong input, try again: ")
if choice == "1":
    trapezoid()
elif choice == "2":
    parallelogram()
elif choice == "3":
    rectangle()
elif choice == "4":
    square()
elif choice == "5":
    triangle()
elif choice == "6":
    circle()
elif choice == "7":
    print("See you soon, bye!")
    exit()



