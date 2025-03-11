def create_array(x,y,z,initial_value):
    
   return [[[initial_value for _ in range(x)]for _ in range(y)]for _ in range(z)]

array_3d=create_array(3,4,5,2)
print(array_3d)
