large=None
small=None
sum=0
count=0
avrg=0

for i in [9,41,12,3,74,15]:
    if small is None:
        small=i
    if i<small:
        small=i
    if large is None:
        large=i
    if i>large:
        large=i
    count=count+1
    sum=sum+i
    avrg=sum/count
print(f'The smallest is: {small}')
print(f'The largest is: {large}')
print(f'The sum is: {sum}')
print(f'the count is: {count}')
print(f'the average is: {avrg:.1f}')