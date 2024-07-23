def quickSort (arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        mid = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        return quickSort(left) + mid + quickSort(right)
arr=[12,2,1,77,5,2]

print(quickSort(arr))
    