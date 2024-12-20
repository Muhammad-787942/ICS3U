 #Author : Muhammad Shees Aftab
   #Date made: 12/12/2024
   #Program : Wordle Database Assignment
   #Description : A program that searches for a wordle date or wordle word in a wordle database
   #VARIABLE DICTIONARY :
     #dates (list) = list of the wordle dates
     #words (list) = list of the wordle words
     #order (int) = the month in order of the time it occurs
     #months (list) = list of the months
     #date (string) = string format of the date YYYYMMDD
     #line (string) = line of the file
     #p (string) = the day in string format
     #q (string) = the month in string format
     #r (string) = the year in string format
     #file (object) = the file object to open the file
     #word (string) = the entered word
     #found_date (string) = the found date of the entered word
     #date (string) = the entered string
     #found_word (string) = the found word of the entered date
     #min_date (int) = the minimum of the found wordle
     #max_date (int) = the maximum of the found word in the wordle
     #d_or_w (string) = asking the user if they find a word or a date
# List to store dates and words
dates = []
words = []

# Function to merge day, month, and year into a single integer date
def merge(p, q, r):
    order = 0
    # List of month abbreviations for conversion
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Loop through the months to find the corresponding month number
    for i in range(len(months)):
        if months[i].lower() == q.lower():
            order = i + 1

    # Format month and day to two digits, then combine year, month, and day into a date string
    order = f"{order:02d}"
    p = f"{int(p):02d}"
    date = f"{r}{order}{p}"
    return int(date)

# Function to read data from the file and populate the dates and words lists
def scanfile():
    try:
        # Open the file 'wordle.dat' for reading
        file = open('wordle.dat', 'r')
        # Read each line in the file
        for line in file:
            # Split the line into month, day, year, and word
            month, day, year, word = line.split()
            # Convert the day, month, and year into a merged date integer
            date = merge(day, month, year)
            dates.append(date)
            words.append(word)
        # Close the file after reading
        file.close()
    except FileNotFoundError:
        # Handle case when the file is not found
        print("File Error: File Not Found")


# Function to search for a word and return the corresponding date
def search_by_word(word):
    # Loop through the words list and check if any word matches the search
    for i in range(len(words)):
        if words[i].lower() == word.lower():
            found_date = dates[i]
            return word, found_date
    return word, None  # Return None if the word is not found

# Function to search for a date and return the corresponding word
def search_by_date(date):
    # Loop through the dates list and check if any date matches the search
    for i in range(len(dates)):
        if dates[i] == date:
            found_word = words[i]
            return date, found_word
    return date, None  # Return None if the date is not found

# Read data from file and populate lists
scanfile()

# Define the earliest and latest valid dates for the range
min_date = int(merge("19", "Jun", "2021"))
max_date = int(merge("21", "Apr", "2024"))

# Welcome message
print("Welcome to the Wordle Database!")

# Ask user to choose whether to search by word or date
d_or_w = input("Enter w if you are looking for a word, or d for a word on a certain date: ")

# If user chooses to search by date
if d_or_w.lower() == 'd':
    try:
        # Ask user to input the year, month, and day
        year = input("Enter the year: ")
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day = input("Enter the day: ")

        # Merge the day, month, and year into a single date integer
        date = merge(day, month, year)

        # Check if the date is within the valid range
        if int(date) < min_date:
            print(f"{date} is too early. No wordles occurred before {min_date}. Enter a later date.")
        elif int(date) > max_date:
            print(f"{date} is too recent. Our records only go as late as {max_date}. Please enter an earlier date.")
        else:
            # Search for the word on the given date
            date, word = search_by_date(date)
            if word:
                print(f"The word entered on {date} was {word}.")
            else:
                print(f"No word found for the date {date}.")
    except ValueError:
        # Handle invalid input for date
        print("Please Enter Valid Input")

# If user chooses to search by word
elif d_or_w.lower() == 'w':
    # Ask user for the word they are searching for
    word = input("What word are you looking for? ")
    word, date = search_by_word(word)
    if date:
        # If the word is found, display the corresponding date
        print(f"The word {word.upper()} was the solution to the puzzle on {date}.")
    else:
        # If the word is not found, display a message
        print(f"{word.upper()} was not found in the database.")

# Handle case where the input is neither 'd' nor 'w'
else:
    print("Please Enter Valid Input")
