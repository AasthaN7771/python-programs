
def program10():
    l=int(input("enter the length of rectagle:"))
    b=int(input("enter the breadth of rectagle:"))
#calculation of area and perimeter
    a=l*b
    p=2*(l+b)
    if a>p:
         print(" area of rectagle is greater than its perimeter")
    else:
         print(" area of rectagle is smaller than its perimeter")


program10()