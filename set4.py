names= {"akshar","bumrah","akashdeep","boult"}
namesA=set()
namesB=set()
for name in names:
    if name.startswith('a'):
       namesA.add(name)
    elif name.startswith('b'):
       namesB.add(name)


print("names starting with A :",namesA)
print("names starting with B :",namesB)
