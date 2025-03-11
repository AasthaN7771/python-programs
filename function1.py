def count_lower_upper(string):
    counts={'lowercase':0,'úppercase':0}
    for char in string :
        if char.islower():
           counts ['lowercase']+=1
        elif char.isupper():
           counts['úppercase']+=1
    return counts
sample= 'My name is Aastha'
result=count_lower_upper(sample)
print('lowercase and uppercasecount :',result)
