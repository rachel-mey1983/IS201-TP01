# ) Print the following patterns using loop. Do not use direct print statements with multiple stars in a single print statement as shown below. You need to create a set of rules to print the pattern.

def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(' ', end='')
        # Print stars
        for k in range(2 * i - 1):
            print('*', end='')
        # Move to the next line after each row
        print()

# Number of rows for the pyramid
rows = 5
print_pyramid(rows)
