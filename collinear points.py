x1=int(input(" 1st x coordinate:"))
x2=int(input(" 2st x coordinate:"))
x3=int(input(" 3st x coordinate:"))
y1=int(input("1st y coordinate:"))
y2=int(input(" 2st y coordinate:"))
y3=int(input(" 3st y coordinate:"))
if (y2-y3)*x1+(y3-y1)*x2+(y1-y2)*x3==0 :
    print( " three points are in same line :")
else:
    print ( " the given three points are not in a straight line ")