def vowels(s):
    if len(s)==0:
        return 0
    first_char=s[0].lower()
    if first_char in 'aeiou':
        return 1 + vowels(s[1:])
    else:
        return vowels(s[1:])
    
input_string=input("enter a string ")
vowel_count=vowels(input_string)
print(f'the number of vowels in the string is : {vowel_count}')
