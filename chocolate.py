#CHOCOLATE JARS
#input:10 20 30
    #  3
#output:21

a=list(map(int,input().split()))
jars=int(input())
A=0
for i in a:
        A=A+(i//3)
        if i%3!=0:
            A=A+1
        else:
            A=A+0       
print(A)
        
    
