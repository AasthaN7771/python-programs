import random
rnum=set(random.randint(15,45)for _ in range(10))
lessthan30=sum(1 for number in rnum if number < 30)
print("original set :",rnum)
print("count of numbers less than 30 :",lessthan30)
rnum={number for number in rnum if number <35 }
print("set ater deleting numbers greater than 35 :",rnum)
