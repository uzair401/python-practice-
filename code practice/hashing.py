def frequencyCount(arr, N, P):
    hash = {}
    
    for i in range(N):
        if arr[i] <= P:
            if arr[i] in hash:
                hash[arr[i]] += 1
            else:
                hash[arr[i]] = 1
    arr = []
    for i in range(1, P + 1):
        arr.append(hash.get(i, 0))
    
    return arr

arr = [2, 2, 3 , 4, 5]
print(frequencyCount(arr, 5, 5))
