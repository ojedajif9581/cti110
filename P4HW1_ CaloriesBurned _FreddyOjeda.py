# calculates the amount of calories burned
# July 6 2019
# CTI-110 P4HW1 - Calories Burned
# Freddy Ojeda
# Type the formula assuming the user burn 5 calories per minute.
# Using a loop to display the number of calories burned after 20,35,45 minutes.
# Display Number of calories burned after time in the treadmill with 5 cpm.
cpm = 5
for minutes in (20, 35, 45):
    print("Number of calories burned after",minutes,"minutes =",(minutes*cpm))
