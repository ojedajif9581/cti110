#Areas of Rectangle
#Input the length and width of rectangle 1.
#Input the length and width of rectangle 2.
#Calculate the area of rectangle 1.
#Calculate the area of rectangle 2.
#if area 1>area2
#Display "Rectangle 1 has the greates area"
#else if area2>area1
#Display"Rectangle 2 has the greates area".
#else
#Display"Both rectangles have the same area".
#Get the dismensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#Get the dimensions of rectangle 2.
length2 = int(input('Enter th length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate the areas of rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:    
    if area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')
