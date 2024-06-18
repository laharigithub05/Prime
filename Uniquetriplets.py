#Unique triplets
#input:7
    # 5 3 20 10 1 4 2
    # 60
#output:3

t=60
p=1
c=0
a=[5,3,20,10,1,4,3]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            print("indexes",i,j,k)
            print("values",a[i],a[j],a[k])
            p=a[i]*a[j]*a[k]
            if p==t:
                print(p)
                print("triplet",a[i],a[j],a[k])
                c=c+1
        print()
print(c)
                
            
