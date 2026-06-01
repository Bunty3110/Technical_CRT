def linear_search(arr, target, size):
    for i in range(size):
        if arr[i] == target:
            return i
    return -1
arr=[1, 2, 3, 4, 5,6,7,8,9,10]
size=len(arr)
target= 7
index=linear_search(arr,target,size)
if(index>0):
    print(f"Element {target} is at index: {index}")
else:
    print("Element not found")