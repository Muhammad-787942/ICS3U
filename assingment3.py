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
#  - Uses the turtle object to plot the entire image.
#  - Parameters:
#       t: The turtle object.
#       cols, rows: Dimensions of the image.
#       color_dict: Dictionary mapping symbols to colors.
#       image_data: List of strings representing the image.
#       diameter: Diameter of each point (pixel).

#def rotateplotImage(t, cols, rows, color_dict, image_data, diameter, rotate)
#  - Uses the turtle object to plot the entire image rotated.
#  - Parameters:
#       t: The turtle object.
#       cols, rows: Dimensions of the image.
#       color_dict: Dictionary mapping symbols to colors.
#       image_data: List of strings representing the image.
#       diameter: Diameter of each point (pixel).
#       rotate: rotate the image.
# get_valid_filename
# Purpose: 
#   This function prompts the user to input a valid filename. 
#   It attempts to read the file using the `readDataFile` function.
#   If the file is not found or contains invalid data, the user is 
#   prompted to re-enter the filename until a valid file is provided.
# Parameters: None
# Returns:
#   - filename (str): The valid filename entered by the user.
#   - cols (int): The number of columns from the file.
#   - rows (int): The number of rows from the file.
#   - color_dict (list): The color definitions extracted from the file.
#   - image_data (list): The image data (grid) read from the file.
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
    
    colorDefs = []
    for i in range(numColors):
        colorData = fh.readline()
        colorData.strip()
        [sym, c, color] = colorData.split()
        if sym == '~':
            sym = " "
        colorDefs.append([sym, color])
            
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
            color = "grey40"
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            for i in range(len(color_dict)):
               if sym == color_dict[i][0]:
                color = color_dict[i][1]
                plotIt(t, x + x_offset, y_offset - y, diameter, color)

def rotateplotImage(t, cols, rows, color_dict, image_data, diameter, rotate):
    # Calculate the center of the canvas
    x_offset = -cols // 2
    y_offset = rows // 2

    for y in range(len(image_data)):  # Use actual number of rows
        for x in range(cols):
            color = "grey40"
            sym = image_data[y][x]  # Get the symbol at position (y, x)
            for i in range(len(color_dict)):
               if sym == color_dict[i][0]:
                color = color_dict[i][1]
                plotIt(t, -x - x_offset, -y_offset + y, diameter, color)

# Main execution
def get_valid_filename():
    filename = input("Enter the filename: ")
    try:
        # Call readDataFile to read the data from the file
        cols, rows, color_dict, image_data = readDataFile(filename)
        
        # Return the filename along with the data retrieved from readDataFile
        return filename, cols, rows, color_dict, image_data

    except FileNotFoundError:
        # Handle the case when the file is not found
        print("File '" + filename + "' not found. Please enter a correct filename.")
        # Recurse to ask again for the correct filename
        return get_valid_filename()

    except ValueError:
        # Handle the case when the file contains invalid data
        print("The file '" + filename + "' contains invalid data. Please check the file and try again.")
        # Recurse to ask again for the correct filename
        return get_valid_filename()
    
bg_color = input("Enter the background color: ")
diameter = int(input("Enter the diameter of the points: "))
rotate = input("Would you like to rotate your image 180 degrees? (yes/no): ")


# Set up canvas size
canvas_width = 500 #Adjust as needed
canvas_height = 500  # Adjust as needed
turtle.setup(canvas_width, canvas_height)

turtle.bgcolor(bg_color)  # Set background color to user input
turtle.tracer(0, 0)  # Turn off screen updates for faster plotting
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle icon

# Read the data file and plot the image
filename, cols, rows, color_dict, image_data = get_valid_filename()
cols, rows, color_dict, image_data = readDataFile(filename)
print(color_dict)

if rotate == "yes":
    rotateplotImage(t, cols, rows, color_dict, image_data, diameter, rotate)
else:
    plotImage(t, cols, rows, color_dict, image_data, diameter)


# Update the screen and finish
turtle.update()
turtle.done()
