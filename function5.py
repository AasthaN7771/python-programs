def ispangram(s):
    alphaset=set('abcdefghijklmnopqrstuvwxyz')
    s_set=set(s.lower())
    return alphaset<=s_set
sentence1='The quick brown fox jumpsover the lazy dog '
print(f'is pangram ? {sentence1}->{ispangram (sentence1)}')
