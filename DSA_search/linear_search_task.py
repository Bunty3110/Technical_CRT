# arr=[3,4,6,7,2,3,2,4,2]   target=2    output element found and count   else element not found

def linear_search(arr, target, size):
    count=0
    for i in range(size):
        if arr[i] == target:
            count+=1
    if(count>0):
        return count
    else:
        return -1

arr=[3,4,6,7,2,3,2,4,2]
size=len(arr)
target= 2
count=linear_search(arr,target,size)
if(count>0):
    print(f"Element {target} is found and count is: {count}")   
else:    print("Element not found")
