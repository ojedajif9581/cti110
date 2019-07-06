# A brief description of the project
# July 6 2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Freddy Ojeda
# Program that displays a table of pounds  starting from 100 through 300 (with a step value of 10) and their equivalent kilograms
# Input the condition formula,using indentation.
# Input data (numbers wanted to be converted in to kilograms in this case is limited from 100 to 300)
# Input funtion formula (Conversion Pounds)
# Calculate using the formula 1KG divided by 2.2046 implementing the return stament so immediately the value from the funtion stops being executed. 
# Use a loop to display the tables from 100 to 300/
        
if __name__== '__main__':
    data = [100, 300]

    def conversion(pound):
        return pound // 2.2046
    for pound in range (100,300,10):
        print(int(conversion(pound)))
