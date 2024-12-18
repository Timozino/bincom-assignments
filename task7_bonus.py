

### Recursive searching algorithm
def recursive_search(arr, target, index=0):
    if index == len(arr):
        return -1  # Target not found
    if arr[index] == target:
        return index  # Target found
    return recursive_search(arr, target, index + 1)


arr = [1, 2, 3, 4, 5]
target = 3
print(f"Found target at index: {recursive_search(arr, target)}")
