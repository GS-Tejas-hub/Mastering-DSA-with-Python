def Sum_Of_array(arr, index=0):
    if index == len(arr):
        return 0
    else:
        return arr[index] + Sum_Of_array(arr, index+1)
arr = [8,7,1,1,9,8]
print(Sum_Of_array(arr))