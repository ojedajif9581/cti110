# CTI-110 
# P3HW2 - MealTipTax 
# FreddyOjeda 
# June292019
#Declare variables.
PERCENT_SALES_TAX = 0.07
#Ask for the price of the food and tip:
foodCharge = float(input("What is the price of the food?:"))
askfortip = float(input("What is the tip IN DECIMAL?: %"))
#Calculate the Tip, Tax, and Total.
if askfortip == 0.15:
    print ('(TIP=15%)')
elif askfortip == 0.18:
    print ('(TIP=18%)')
elif askfortip == 0.20:
    print ('(TIP=20%)')
else:
    print ("The tip amount is: INVALID")
tip = (foodCharge * askfortip)
salesTax = (PERCENT_SALES_TAX)
total = (foodCharge + tip + salesTax)
#Display the Tip, Tax, and Total
print ("The price of food is:", format(foodCharge, ",.2f"))
if tip >= 0.15:
    print ("The tip amount is:", format(tip, ",.2f"))
elif tip >= 0.18:
    print ("The tip amount is:", format(tip, ",.2f"))
elif tip <=0.20:
    print ("The tip amount is:", format(tip, ",.2f"))
else:
    print ("The tip amount is: INVALID")
print ("The sales tax is:", format(salesTax, ",.2f"))
print ("The total amount of the meal is:", format(total, ",.2f"))
