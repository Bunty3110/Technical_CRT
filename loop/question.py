n= int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(n-1):
    diff=arr[i]-arr[i+1]
    sum=sum+abs(diff)
print(sum)