names= set()
#adding five names to the set
names.add("rohit")
names.add("virat")
names.add("bumrah")
names.add("charles leclarc")
names.add("louis hamilton")
print ('set after adding names :',names)
if "virat"in names :
    names.remove("virat")
    names.add("harry potter")
    print("set after modifying a name :",names)
names.discard("charles leclarc")
names.discard("louis hamilton")
print("set after discarding two names :",names) 
