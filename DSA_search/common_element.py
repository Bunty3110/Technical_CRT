arr1=[1,2,3,4,5]
arr2=[5,6,7,8,9]
arr3=[]
for i in arr1:
    if i in arr2:
        arr3.append(i)
print(arr3)