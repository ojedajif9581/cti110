# Sum of Numbers
# July 6 2019
# CTI-110 P4HW3 - Sum of Numbers
# Freddy Ojeda
# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.
print("Enter positive numbers until you wish to stop then enter a negative number")
count = 0
fcount = 0
while count >= 0:
  count = int(input("Please input a number: "))
  if count >= 0:
    fcount += count
print("The sum of all entered numbers is:", fcount)
