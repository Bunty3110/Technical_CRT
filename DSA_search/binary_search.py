def binarySearch(arr,size,target):
    low = 0
    high = size-1
    swith=0
    if(arr[low]==target):
         swith=1
         print(f"{target} is found at {low}")
    if(arr[high]==target):
         swith=1
         print(f"{target} is found at {high}")
    while swith==0:
         mid=(low+high)//2
         if(arr[mid]==target):
              print(f"{target} is found at {mid}")
              swith=12
              break
         elif(arr[mid]>target):
              high=mid-1
         elif(arr[mid]<target):
              low=mid+1
         
    

# arr=list(map(int, input().split()))
arr=[1,2,3,4,5,6,7,8,9,12,14,15,17,18,19,36,56,67,69,73,122,136,145,168,245,254,353,389]
size=len(arr)
target=int(input())
binarySearch(arr,size,target)

