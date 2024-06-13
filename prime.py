# input: an integer value N
#output: return an integer value representing smallest prime number larger than N


def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input())
k=num+1
while True:
    if isprime(k):
        print(k)
        break
    k=k+1
    
        
        
    
