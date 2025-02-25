def names(words_list):
    upper_set=set()
    for word in words_list:
        upper_set.add(word.upper())
    return upper_set
words=['rohit','virat','bumrah']
upper_set=names(words)
print(upper_set)
