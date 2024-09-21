def reverseArray(arr):
        if len(arr) <= 1:
            return arr
        
        first_element = arr[0]
        reversed_rest = reverseArray(arr[1:])
        reversed_rest.append(first_element)
        
        return reversed_rest

list = [1,2,2,3,4,5,43,32,24,54,2,3]
print(reverseArray(list))