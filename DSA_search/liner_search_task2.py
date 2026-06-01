# arr=[3,4,6,7,2,3,2,4,2,2,2,2,2]   target=2    output element found and last element index  else element not found

def linear_search(arr, target, size):
    index=-1
    for i in range(size):
        if arr[i] == target:
            index=i
    return index

arr=[3,4,6,7,2,3,2,4,2,2,2,2,2]
size=len(arr)
target= 2
index=linear_search(arr,target,size)
if(index>-1):
    print(f"Element {target} is found at last index: {index}")   
else:    print("Element not found")
