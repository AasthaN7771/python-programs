import math

def point_in_circle(x_center, y_center, radius, x_point, y_point):
    # Calculate the distance between the center and the point
    distance = math.sqrt(math.pow((x_point - x_center), 2) + math.pow((y_point - y_center), 2))
    
    if distance < radius:
        print("The point lies inside the circle.")
    elif distance == radius:
        print("The point lies on the circle.")
    else:
        print("The point lies outside the circle.")

x_center = float(input("Enter the x coordinate of the center of the circle: "))
y_center = float(input("Enter the y coordinate of the center of the circle: "))
radius = float(input("Enter the radius of the circle: "))
x_point = float(input("Enter the x coordinate of the point: "))
y_point = float(input("Enter the y coordinate of the point: "))

point_in_circle(x_center, y_center, radius, x_point, y_point)
