# This program converts kilometers to miles.
# July 12 2019.
# CTI-110 P5T1_KilometerConverter 
# Ojeda Freddy
# This program converts kilometer to miles.
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# The show_miles funtion to convert it.
def main():
    #Get the distance in kilometers.
    kilometers = float (input('Enter a distance in kilometers: ' ))
    
    #Display the distance converted to miles.
    show_miles(kilometers)
    
#The show_miles function converts the parameter km from
# Kilometers to miles and displays the results.
def show_miles(km):
    #calculate miles.
    miles = km * CONVERSION_FACTOR
    
    #Display the miles.
    print(km, 'kilometers equals', miles,'miles.')
    
#Call the main function.
main()
