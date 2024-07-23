def Binary_Search(arr, high, low, target):
    mid = (low+high)//2
    if low > high:
        return -1
    elif arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return Binary_Search(arr, mid - 1, low, target)
    else:
        return Binary_Search(arr, high, mid + 1, target)
arr = [1,2,3,4,5,6]
target = 4/2

result = Binary_Search(arr, len(arr)-1, 0, target)    
print(result)