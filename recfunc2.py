def recbinaryequi():
    n=int(input('enter a number'))
    if n < 0:
        print('enter a positive number')
        return
    binary=""
    while n >0 :
        remainder=n%2
        binary=str(remainder)+binary
        n=n//2
        print(f'the binary equivalent is : {binary}')
     
recbinaryequi()
