#basketball
#input:5
    #  2
    #  1 2 3 4 5
#output:14

shots=int(input())
subarr=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-subarr+1):
    temp=arr[i:i+subarr]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)
    
