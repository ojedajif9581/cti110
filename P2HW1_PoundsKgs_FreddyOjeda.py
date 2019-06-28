#This program converts pound to kilograms
#Ojeda Freddy
#June 24 2019
#Input the condition formula,using indentation.
#Input data (numbers wanted to be converted in to kilograms)
#Input funtion formula (Convert Pounds)
#Calculate 1kg = 2.2lb using the formula 1KG divided by 2.2046 implementing the return stament so immediately the value from the funtion stops being executed. 
#Using a for Loop so the program can provide a shorcut
#Pounds to Kilograms:
if __name__== '__main__':
    data = [3, 1010, 175, 1516]

    def conversion(pound):
        return pound // 2.2046
    for pound in data:
        print(int(conversion(pound)))
