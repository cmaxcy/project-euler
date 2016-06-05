"""
    Project Euler Problem 11: Largest Product in a grid
    A given grid of numbers is to be searched to find the largest multiple of 4 adjacent numbers
    Adjacent groups must lie solely on the same row, column, or diagonal
"""


# takes in a string of numbers separated by spaces, and returns a list of the numbers
# assumes string contains solely ints separated by spaces
def line_to_nums(line):

    # containers for the numbers in both string and integer forms
    string_list = line.split()
    int_list = []

    # add the integer version to int_list of each number string in string_list
    for string in string_list:
        int_list.append(int(string))

    return int_list


# reads the file passed and retrieves the 2 dimensional int list from it
# uses line_to_nums and assumes its conditions are met
# assume file passed exists and contains a valid square int grid
def file_to_grid(file_name):

    # used to read the file
    file_reader = open(file_name, 'r')

    # used to form grid
    num_grid = []

    # go through file and add each line to the the grid
    # use line_to_nums to extract the int list from each line
    for line in file_reader:
        num_grid.append(line_to_nums(line))

    return num_grid


# finds the largest multiple from a combination of 4 vertically adjacent numbers
# assumes valid square 2 dimensional int grid passed
def find_max_col(grid):

    # maximum combination multiple found (initially -1)
    max_multiple = -1

    # for each location but 3 one the y-axis, and each location on the x
    for y in range(len(grid) - 3):
        for x in range(len(grid[y])):

            # stores current group's multiple (reset to 1 each time x loop iterates)
            this_multiple = 1

            # multiplies each of the 4 numbers in this column group together
            for i in range(4):
                this_multiple *= grid[y + i][x]

            # replace max_multiple if bigger candidate found
            if this_multiple > max_multiple:
                max_multiple = this_multiple

    return max_multiple


# finds the largest multiple from a combination of 4 horizontally adjacent numbers
# assumes valid square 2 dimensional int grid passed
def find_max_row(grid):

    # maximum combination multiple found (initially -1)
    max_multiple = -1

    # for each location on the y-axis, and each location but 3 on the x-axis
    for y in range(len(grid)):
        for x in range(len(grid[y]) - 3):

            # stores current group's multiple (reset to 1 each time x loop iterates)
            this_multiple = 1

            # multiplies each of the 4 numbers in this row together
            for i in range(4):
                this_multiple *= grid[y][x + i]

            # replace max_multiple if bigger candidate found
            if this_multiple > max_multiple:
                max_multiple = this_multiple

    return max_multiple


# finds the largest multiple from a combination of 4 diagonally adjacent along the same line
# assumes valid square 2 dimensional int grid passed
def find_max_diag(grid):

    # maximum combination multiple found (initially -1)
    max_multiple = -1

    # \ diagonal
    # for each location but the last 3 on the y-axis, and each location but last 3 on the x-axis
    for y in range(len(grid) - 3):
        for x in range(len(grid[y]) - 3):

            # stores current group's multiple (reset to 1 each time x loop iterates)
            this_multiple = 1

            # multiplies each of the 4 numbers on the \ diagonal together
            for i in range(4):
                this_multiple *= grid[y + i][x + i]

            # replace max_multiple if bigger candidate found
            if this_multiple > max_multiple:
                max_multiple = this_multiple

    # / diagonal
    # for each location but the last 3 on the y-axis, and each location but the first 3 on the x-axis
    for y in range(len(grid) - 3):
        for x in range(3, len(grid[y])):

            # store's current group's multiple (reset to 1 each time x loop iterates)
            this_multiple = 1

            # multiplies each of the 4 numbers on the / diagonal together
            for i in range(4):
                this_multiple *= grid[y + i][x - i]

            # replace max_multiple if bigger candidate found
            if this_multiple > max_multiple:
                max_multiple = this_multiple

    # return maximum of both diagonal (\ and /) checks
    return max_multiple


# finds the largest multiple from a combination of 4 vertically, horizontally, or diagonally adjacent numbers
# uses find_max_col, find_max_row, and find_max_diag
# assumes valid square 2 dimensional int grid passed
def find_max_multiple(grid):

    # stores the maximum from each direction
    directions = [find_max_col(grid), find_max_row(grid), find_max_diag(grid)]

    # returns the maximum directional multiple found
    return max(directions)


# finds the largest multiple group from the int grid in the file
# uses find_max_multiple, file_to_grid, and all functions contained within them
# all used function assumptions present
def file_to_mult(file_name):
    return find_max_multiple(file_to_grid(file_name))


print(file_to_mult("numGrid.txt"))

