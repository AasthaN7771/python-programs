def reverse_list(numbers):
    if len(numbers)<= 1:
         return numbers

    return reverse_list(numbers[1:])+[numbers[0]]
    
numbers=[1,2,3,4,5]
reversed_numbers=reverse_list(numbers)
print('original list :',numbers)
print('reversed list :',reversed_numbers)
