def sum_avg(sub1,sub2,sub3,sub4,sub5):
    marks=[sub1,sub2,sub3,sub4,sub5]
    total=sum(marks)
    average=total/len(marks)
    return total,average
total,average=sum_avg(45,18,77,7,67)
print(f'total marks:{total}')
print(f'average marks:{average}')

