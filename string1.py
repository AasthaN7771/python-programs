

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Accept the string from the user
a = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(a)}")
