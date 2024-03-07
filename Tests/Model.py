home_a = (-6, -6)

# format: shelving unit_location on shelf
# ex: A1_1
warehouse_location = str(input("Please enter the desired location: "))

# defines where the robot starts
x_position = home_a[0]
y_position = home_a[1]

# update the robots position within the warehouse
def update_position(dx, dy):
    global x_position
    global y_position

    x_position += dx
    y_position += dy

# returns the x and y position of the robot
def get_positon():
    global x_position
    global y_position
    return x_position, y_position


'''
These functions are all associated 
with finding the coordinates of where 
the box is in the warehouse
'''
def x_location_from_letter(letter):
    # find x_coord based on letter
    if(letter == "A" or letter == "C"):
        return 12
    else:
        return 60

def y_location_from_letter(letter):
    # find y_coord based on letter
    if(letter == "A" or letter == "B"):
        return 12
    else:
        return 60

def y_location_adjustment_from_shelving_unit_number(unit_number):
    if(unit_number == 2):
        return 24
    return 0

def x_location_adjustment_from_location_on_shelf(location):
    location -= 1
    location = location % 6
    location *= 6
    return location

def y_location_adjustment_from_location_on_shelf(location):
    if(location / 12 > 0.5):
        return 12
    return 0

# shelf location is defined by the bottom left corner of the shelf
def shelving_unit_to_coords(shelving_unit_letter, shelving_unit_number):
    # initial coordinates
    x_coord = x_location_from_letter(shelving_unit_letter)
    y_coord = y_location_from_letter(shelving_unit_letter)

    # change initial coordinates based on if it is the first of second shevling unit
    x_coord += 0
    y_coord += y_location_adjustment_from_shelving_unit_number(shelving_unit_number)

    return x_coord, y_coord

# adjusts the given x and y coordinates based on where the box is on the shelf
def adjust_coords_from_location_on_shelf(x_coord, y_coord, location_on_shelf):
    x_coord += x_location_adjustment_from_location_on_shelf(location_on_shelf)
    y_coord += y_location_adjustment_from_location_on_shelf(location_on_shelf)

    return x_coord, y_coord

# this function will take a warehouse location and convert it into coordinates based on where the box is
def coords_from_warehouse_location(warehouse_location):
    # split the location into its individual parts
    location_string = warehouse_location.split("_")

    # assign the individual parts of the string to the correct variable
    shelving_unit_letter = str(location_string[0][0])
    shelving_unit_number = int(location_string[0][1])
    location_on_shelf = int(location_string[1])

    # calculate the coordinates
    x_coord, y_coord = shelving_unit_to_coords(shelving_unit_letter, shelving_unit_number)
    x_coord, y_coord = adjust_coords_from_location_on_shelf(x_coord, y_coord, location_on_shelf)

    return(x_coord, y_coord)

'''
All of these fuctions are associated with 
calculating the distance and number of turns
needed to get the the desired row and column the box is in
'''
# ranges from 0 - 4
def find_row(y_coord):
    if(y_coord < 18):
        return 0
    if(y_coord < 42):
        return 1
    if(y_coord < 66):
        return 2
    if(y_coord < 90):
        return 3
    return 4

# ranges from 0 - 2
def find_col(x_coord):
    if(x_coord < 12 + 18):
        return 0
    if(x_coord < 60 + 18):
        return 1
    return 2

# calculates the number of times the robot moves straight
def find_straights(row):
    # number of times the robot has to move 12 (in) forward
    straights = 2*row
    
    return straights

# calculates the inches traveled by the robot when going straight
def find_straight_inches(straights):
    inches_traveled = straights * 12
    update_position(0, inches_traveled)
    return inches_traveled

# calculates the error in the x and y direction when going straight
def find_straight_error(y_coord):
    inches_traveled = find_straight_inches(find_straights(find_row(y_coord)))
    
    # return error based on statistics
    if(inches_traveled <= 0):
        return 0, 0
    if(inches_traveled <= 12):
        return 0.00, 0.55
    if(inches_traveled <= 36):
        return -0.84, 1.21
    if(inches_traveled <= 60):
        return -1.17, 2.62
    if(inches_traveled <= 84):
        return 0.50, 3.23
    return inches_traveled*(-0.35/51), inches_traveled*(1.85/51)

# calculates the total inches traveled when going straight,
# turning 90 degrees, then going forward again
def find_straight_then_turns_inches(col):
    # inital forward
    inches_traveled = 12
    update_position(0, inches_traveled)
    
    # inches after the turn
    if(col >= 0):
        inches_traveled += 12
    if(col >= 1):
        inches_traveled += 36
    if(col >= 2):
        inches_traveled += 36
    
    update_position(inches_traveled - 12, 0)

    return inches_traveled

# calculates the error in the x and y direction when going straight
# then turning 90 degrees then going straight again
def find_straight_then_turns_error(x_coord):
    inches_traveled = find_straight_then_turns_inches(find_col(x_coord))

    # return the error based of of the found values
    if(inches_traveled <= 24):
        return 0.35, -0.05
    if(inches_traveled <= 36):
        return 0.47, 0.35
    if(inches_traveled <= 60):
        return -0.55, 1.85
    if(inches_traveled <= 96):
        return -1.45, 5.07
    return inches_traveled*(-0.35/51), inches_traveled*(1.85/51)

# calculates the total error in getting to the row and column the
# desired box is located in
def find_row_col_error(warehouse_location):
    x_coord, y_coord = coords_from_warehouse_location(warehouse_location)

    x_error_1, y_error_1 = find_straight_then_turns_error(x_coord)
    x_error_2, y_error_2 = find_straight_error(y_coord)

    total_x_error = x_error_1 + x_error_2
    total_y_error = y_error_1 + y_error_2

    return total_x_error, total_y_error

print()
starting_position = get_positon()
row_col_error = find_row_col_error(warehouse_location)
row_col_position = get_positon()

print("Starting position: " + str(starting_position))
print("Row/Col Error: " + str(row_col_error))
print("Row/Col Position: " + str(row_col_position))

# find the distace the robot is from the box
x_dist = coords_from_warehouse_location(warehouse_location)[0] - get_positon()[0]
y_dist = coords_from_warehouse_location(warehouse_location)[1] - get_positon()[1] 

# update position to the box
update_position(x_dist, y_dist)

# calculate the error in moving to that location
x_error = row_col_error[0] + (abs(x_dist) * 0.00)
y_error = row_col_error[1] + (abs(y_dist) * (0.55 / 2))

total_error = (x_error, y_error)

print()
print("Total Error: " + str(total_error))
print("Final Posistion: " + str(get_positon()))