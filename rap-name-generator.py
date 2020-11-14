# Guided Exploration No. 3
# Joseph Ferrier

# Import the random library so we can use randint
import random

# Create a blank list which we will append names to later
possible_names = []

# create a file to store our rap names
outputFile = open('rap-names-output.txt', 'w')

# Open the rap names file in read format, and set it as the variable dataFile
with open('rap-names.txt', 'r') as dataFile:
    # Iterate through each line in the data file
    for name in dataFile:
        # Append each name in that file to the possible_names list, removing any line feed
        possible_names.append(name.rstrip())

# define a variable "count" and ask the user how many names they will create. We will use this to know how many times to run a loop
count = int(input('How many rap names would you like to create? '))
# As above, but asking how many words should each full name contain? Again we will use this for a loop
parts = int(input('How many parts should the name contain? '))

# Using the Count variable above, run this loop that number of times. Each loop creates a name.
for i in range(count):
    # Create a list for the name parts, start with it empty.
    name_parts = []
    # Run this loop as many times as the user specified in the second input. Each loop adds one part to a rap name
    for j in range(parts):
        # Append a random name to name_parts from the possible names list.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # Write each rap name to the file. Join the list into a string using space as a seperator, and after each name, enter a line break
    outputFile.write(f"{' '.join(name_parts)} \n")
    # Print as above
    print(f"{' '.join(name_parts)}")

# close the file
outputFile.close()
