# Muhammad Shees Aftab
# December 3rd 2024
# XPM File Renderer with Turtle Graphics
#This program reads an XPM file, parses its content, and renders the image
#using Python's `turtle` graphics module. The image is constructed point by 
#point using the color definitions provided in the XPM file.

#Functions:
#----------
#plotIt(T, x, y, d, color):
#  - Plots a single point on the screen using the turtle object.
#- Parameters: T: The turtle object. x, y: Coordinates where the point should be plotted. d: Diameter of the point. color: Color of the point.

#readDataFile(filename):
 #  - Reads and parses the XPM file.
 #  - Extracts:
 #      * Image dimensions (columns, rows).
 #      * Number of colors and their definitions.
 #      * The pixel data of the image.
 #  - Returns:
 #      * Number of columns and rows.
 #      * Dictionary mapping symbols to colors.
 #     * The image data as a list of strings.

#plotImage(t, cols, rows, color_dict, image_data, diameter):
#   - Uses the turtle object to plot the entire image.
#  - Parameters:
#       t: The turtle object.
#       cols, rows: Dimensions of the image.
#       color_dict: Dictionary mapping symbols to colors.
#       image_data: List of strings representing the image.
#       diameter: Diameter of each point (pixel).

filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")
colorData = fh.readline() # file handle must be open
colorData.strip() 

print(colorData)

rows, cols, numColors = colorData.split()

numColors=int(numColors)

colorDefs = []
for i in range(numColors):
    colorData = fh.readline()
    colorData.strip()
    [sym, c, color] = colorData.split()
    if (sym == '~'):
        sym = " "
    colorDefs.append([sym, color])
    print(i, sym, color)

print(colorDefs)

import turtle

def plotIt(T, x, y, d, color):
    # T is the turtle object
    # (x, y) are the coordinates
    # d is the diameter of the point
    # color is the color of the point
    T.penup()  # Raise the pen to prevent drawing while moving
    T.goto(x, y)  # Move to the specified coordinates
    T.pendown()  # Lower the pen to start drawing
    T.dot(d, color)  # Draw a dot of specified diameter and color
    T.penup()  # Raise the pen again after drawing the dot

def readDataFile(filename):
    fh = open(filename, "r")
    colorData = fh.readline().strip()
    
    print(colorData)
    
    # Adjust to handle the possibility of four values
    values = colorData.split()
    if len(values) == 4:
        cols, rows, numColors, _ = values  # Ignore the fourth value
    else:
        cols, rows, numColors = values  # Handle the usual case
    
    cols, rows, numColors = int(cols), int(rows), int(numColors)
    
    colorDefs = {}
    for i in range(numColors):
        colorData = fh.readline().strip()
        sym, c, color = colorData.split()
        if sym == "~":
            sym = " "
        colorDefs[sym] = color
    
    print(colorDefs)
    
    # Read the image data
    image_data = []
    for _ in range(rows):
        line = fh.readline().rstrip()  # Read each line of the image data, removing trailing spaces
        if line:  # Skip empty lines
            image_data.append(line)
    
    fh.close()
    
    # Return columns, actual rows, color definitions, and image data
    return cols, len(image_data), colorDefs, image_data

def plotImage(t, cols, rows, color_dict, image_data, diameter):
    # Calculate the center of the canvas
    x_offset = -cols // 2
    y_offset = rows // 2

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            color = color_dict.get(sym, "gray40")  # Get the corresponding color or default to gray40
            plotIt(t, x + x_offset, y_offset - y, diameter, color)  # Plot the point with adjusted coordinates

def plotRotatedImage(t, cols, rows, color_dict, image_data, diameter, angle):
 # Plots the rotated image using the turtle graphics module.
 rotated_pixels = rotateImage(cols, rows, image_data, angle)

    x_offset = -cols // 2  # Adjust for turtle coordinates
    y_offset = rows // 2

    for x, y, sym in rotated_pixels:
        if 0 <= x < cols and 0 <= y < rows:  # Ensure within bounds
            color = color_dict.get(sym, "gray40")  # Get the color or default to gray40
            plotIt(t, x + x_offset, y_offset - y, diameter, color)
 
# Main execution
filename = input("Enter the filename (smiley_emoji_mod.xpm): ")
bg_color = input("Enter the background color (black): ")
diameter = int(input("Enter the diameter of the points (8): "))

# Set up canvas size
canvas_width = 500 #Adjust as needed
canvas_height = 500  # Adjust as needed
turtle.setup(canvas_width, canvas_height)

turtle.bgcolor(bg_color)  # Set background color to user input
turtle.tracer(0, 0)  # Turn off screen updates for faster plotting
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle icon

# Read the data file and plot the image
cols, rows, color_dict, image_data = readDataFile(filename)
plotImage(t, cols, rows, color_dict, image_data, diameter)

# Update the screen and finish
turtle.update()
turtle.done()
