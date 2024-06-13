#diwali contest
#input:6
    #  180
#output:4

p=int(input())
time=int(input())
count=0
sum=0
rt=4*60-time
for i in range(1,p+1):
    sum=sum+5*i
    if sum>rt:
        break
    count=count+1
print(count)
