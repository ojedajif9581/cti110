#CTI-110 
# P3HW1 - Color Mixer 
# Freddy Ojeda 
# June 26 2019
# Prompt the user to enter the first name of the first primary color
# Prompt the user to enter the second name of the second primary color
# Assign the codes of each name of colors
# red equals red, blue equals blue, yellow equals yellow
# Using Boolean logic, implement the if-elif-else statement to make the decision structure for the primary colors to mix.
# Close the block of the stament with an error message letting the user know that a primary color is not written.
primary_color1 = input("Enter primary color 1 :")
primary_color2 = input("Enter primary color 2 :")
red="red"
blue="blue"
yellow="yellow"

if (primary_color1 == red and primary_color2 == blue) or  (primary_color1 == blue and primary_color2 == red):
    print("When you mix red and blue, you get purple.")

elif (primary_color1 == blue and primary_color2 == yellow) or (primary_color1 == yellow and primary_color2 == blue):
    print("When you mix blue and yellow, you get green.")

elif (primary_color1 == yellow and primary_color2 == red) or (primary_color1 == red and primary_color2 == yellow):
  print("When you mix yellow and red, you get orange.")

else: 
  print("Error NO primary color inserted.")
