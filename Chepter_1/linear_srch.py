def search(arr, target):
    n = len(arr)
    
    # Iterate linearly through the array
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 7, 1, 5]
    target = 7
    index = search(arr, target)
    print(index)
