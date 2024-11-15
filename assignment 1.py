import math
#Allows user to give a value to "length"
length = input("please input a length for a rectangle: ")
#Allows user to give a value to "width"
width = input("please input width for a rectangle: ")
#Defines "length" as an integer
length = int(length)
#Defines "width" as an integer
width = int(width)
#Provides a formula for "area1" with the given inputs
area1 = length * width
#Prints the result of area1 with the inputted values
print ("the area of the rectangle is: ", area1)

#Allows user to input a value for "radius"
radius = input("please input a radius for a circle here: ")
#Defines radius as an integer
radius = int(radius)
#Provides the formula for "area2" with the given inputs
area2 = math.pi * math.pow (radius,2)
#Prints the result of "area2" with the inputted values
print("The area of a circle of radius is %.2f" % area2)

#Allows user to give "height" a value
height = input("please input a height for a cylinder: ")
#Allows user to give "radius2" a value
radius2 = input("please input a radius for a cylinder: ")
#Defines "height" as an integer
height = int(height)
#Defines "radius2" as an integer
radius2 = int(radius2)
#Provides formula for "volume" with the given inputs
volume = math.pi * math.pow (radius2,2) *height
#Provides formula for "surface_area" with the given inputs
surface_area = (2 * math.pi * radius2 * height) + (2 * math.pi * math.pow (radius2,2))
#Prints result of "surface_area" with the given inputs to the second decimal point
print ("The surface area of a cylinder is %.2f" % surface_area)
#Prints result of "volume" with the given inputs to the second decimal point
print ("The volume of a cylinder is %.2f" % volume) 

#Gives value to the variable "g"
g = 9.8
#Allows user to input a value for "length2"
length2 = input("please input a value for length in meters: ")
#Defines "length2" as an integer
length2 = int(length2)
#Provides a formula for "period" with the given inputs
period = 2 * math.pi * math.sqrt(length2/g)
#Prints the result of "period" with the given inputs to the second decimal point
print ("The period it takes for the pendulum to make one full turn is %.2f " % period) 
