home_a = (-6, -6)

# format: shelving unit_location on shelf
# ex: A1_1
warehouse_location = str(input("Please enter the desired location: "))

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
needed to get the the desired box location
'''

def find_row(y_coord):
    if(y_coord < 18):
        return 1
    