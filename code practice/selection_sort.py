def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [1,3,4,5,19,20,21,45,50,3,4,5,6,7]
arr1 = [9,8,7,6,6,4,3,2,1]
print(selection_sort(arr1))


