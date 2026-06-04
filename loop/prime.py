def primeCheck(i):
    for k in range(2,i//2):
        if(i%k==0):
            return False
    return True
n=int(input())
m=int(input())
arr=[]
for i in range(n,m):
    if(primeCheck(i)):
        arr.append(i)
print(arr)

