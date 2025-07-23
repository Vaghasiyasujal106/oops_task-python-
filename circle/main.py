#Define a class for a Circle with methods to calculate its area and circumference
from math import pi

class Circle:
 def __init__(self,radius):
  self.radius = radius

 def area(self):
  area1 = pi * self.radius * self.radius
  return area1

 def circumference(self):
  circumference1 = 2 * pi * self.radius
  return circumference1

radius = float(input("Enter the radius of the circle: "))
c1 = Circle(radius)
while True:
    print("1.area of the circle:")
    print("2.circumference of circle:")
    print("3.exit the code....")

    try:
        choice = int(input("enter the choice:"))
        if choice == 1:
            print(f" area of the circle :{c1.area()}")
        elif choice == 2:
            print(f" circumference of the circle :{c1.circumference()}")
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

