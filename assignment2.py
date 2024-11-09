import math
# Made by Muhammad Shees Aftab
# School Yearbook Program
# This program calculates the optimal layout dimensions (rows and columns) 
# for a given number of photos to obtain the smallest perimeter, making 
# the arrangement as compact as possible. Users can enter multiple photo 
# counts and view a summary of the best layouts at the end.
# Functions:
#   - get_valid_input(): Repeatedly prompts user input until a valid positive 
#     integer or "done" is entered.
#   - find_best_dimensions(): Calculates the layout (rows x columns) with 
#     the smallest perimeter for given photos.
#   - main(): Runs the primary program loop, handling user interaction, 
#     storage, and summary of results.

def get_valid_input():
    while True:
        user_input = input("Input a number of photos (or type 'done' to finish): ")
        
        # Check if the user wants to exit
        if user_input.lower() == "done":
            print("Exiting the program.")
            return None
        
        try:
            # Convert input to an integer
            number_of_photos = int(user_input)
            if number_of_photos >= 1:
                return number_of_photos
            else:
                print(f"{number_of_photos} is not a valid number. "
                      "Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'done' to exit.")

def find_best_dimensions(total_photos):
    # Initialize the best perimeter to None for comparison
    best_perimeter = None  
    # Start with default layout of 1 row x total_photos columns
    best_dimensions = (1, total_photos)  
    
    # Check divisors of total_photos to find possible row and column combinations
    for rows in range(1, int(math.sqrt(total_photos)) + 1):
        # Rows must divide total_photos evenly
        if total_photos % rows == 0:  
            columns = total_photos // rows
            # Calculate perimeter for current layout
            perimeter = 2 * (rows + columns)  
            
            # Update the best perimeter and dimensions if this perimeter is smaller
            if best_perimeter is None or perimeter < best_perimeter:
                best_perimeter = perimeter
                best_dimensions = (rows, columns)
                
    return best_dimensions, best_perimeter

def main():
    print("Welcome to the school yearbook program!")
    
    # Lists to store all layout details for summary
    layout_dimensions = []
    layout_perimeters = []
    photo_counts = []
    
    while True:
        # Get valid user input or None if exiting
        number_of_photos = get_valid_input()
        # Exit the loop if "done" was entered
        if number_of_photos is None:
            break
        
        # Calculate the best layout for the current number of photos
        best_dimensions, best_perimeter = find_best_dimensions(number_of_photos)
        rows, columns = best_dimensions
        
        # Store the layout results for later summary
        layout_dimensions.append(best_dimensions)
        layout_perimeters.append(best_perimeter)
        photo_counts.append(number_of_photos)
        
        # Display the best layout for the current number of photos
        print(f"The best layout for {number_of_photos} photos is {rows} x {columns} "
              f"with a perimeter of {best_perimeter}.")
# Run the program
main()
