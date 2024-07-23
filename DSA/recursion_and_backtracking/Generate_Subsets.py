def generate_subsets(arr, index=0, current=[]):
    if index == len(arr):
        print(current)
        return
    generate_subsets(arr, index + 1, current)
    generate_subsets(arr, index + 1, current + [arr[index]])
arr = [1, 2, 3, 4]
generate_subsets(arr)