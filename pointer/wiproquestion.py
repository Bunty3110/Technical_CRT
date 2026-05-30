
number=int(input())
key=0
freq=[0]* 10
while(number>0):
    
    freq[number%10]+=1
    number=number//10
for i in range(10):
    if(freq[i]>1):
        key+=1
print(key)
