names_list=['aastha','shreya',('krishna','ronak','bhavya')]
boys_count=0
girls_count=0
for name in names_list:
    if isinstance(name,tuple):
        boys_count += len(name)
    else :
        girls_count += 1
print("number of boys are :",boys_count)
print("number of girls are :",girls_count)
            
        
        
        
