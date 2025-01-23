# Author: Muhammad Shees Aftab
# Student Number: 787942
# Created Date: 17 Jan 2025
# Program: Credit Card Assignment
# Description: Creates a report of expired credit cards from the customer database.

# VARIABLE DICTIONARY:
# filename: str - Name of the input file containing customer data
# fh: file object - File handle for the input file
# names: list - List to store customer full names (first and last)
# cc_nums: list - List to store credit card numbers
# cc_types: list - List to store credit card types (e.g., Visa, MasterCard)
# expiry_dates: list - List to store formatted expiry dates as integers (YYYYMM)
# lines: list - List to store all the lines read from the input file
# first_line: str - The header line of the input file (not used in the program)
# output_file: file object - File handle for the output file where results are written
# expired_text: str - Text indicating the expiry status of the credit card (EXPIRED / RENEW IMMEDIATELY)
# formatted_cc_num: str - The credit card number with a # prefix

# Function to apply the merge sort algorithm to multiple lists.

def mergeSort(arr, arr2, arr3, arr4, l, r):
    # Check if the subarray has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        # Avoids potential overflow for large values of l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)


def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create temp arrays
    L =  [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R =  [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open the input file to read the data
filename = "data.dat"
fh = open(filename, 'r')

# Prepare lists to store customer details
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Read all lines from the file and process the data
lines = fh.readlines()
for line in lines[1:]:  # Skip the header line
    given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
    names.append(given_name + ' ' + surname)  # Combine first and last names
    cc_types.append(cc_type)  # Store the credit card type
    cc_nums.append(cc_number)  # Store the credit card number

    # Convert expiry date to a numeric format (YYYYMM)
    expiry_date = int(exp_yr) * 100 + int(exp_mo)  # Combine year and month
    expiry_dates.append(expiry_date)  # Store the formatted expiry date

fh.close()  # Close the input file

# Sort the data based on the expiry date
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

# Create the output report in a text file
output_file = open("output.txt", "w")
for i in range(len(expiry_dates)):
    if expiry_dates[i] > 202501:  # Stop if the credit card is not expired
        break
    expired_text = "EXPIRED" if expiry_dates[i] < 202501 else "RENEW IMMEDIATELY"  # Set expiration status
    formatted_cc_num = "#" + cc_nums[i]  # Add # before the credit card number
    # Print the results in a formatted manner
    print("%-20s %-20s %-20s %-20s %-100s" % (names[i], cc_types[i], formatted_cc_num, expiry_dates[i], expired_text))
    # Write the results to the output file
    output_file.write("%-20s %-20s %-20s %-20s %-100s\n" % (names[i], cc_types[i], formatted_cc_num, expiry_dates[i], expired_text))

output_file.close()  # Close the output file
