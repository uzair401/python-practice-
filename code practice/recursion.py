def reverseArray(arr):
        length = len(arr)
        x = 1
        r = arr[length-1]
        if x >= r:
            return 0
        arr[x+1] = arr[r-1]
        reverseArray(arr)
        x +=1 
        r += 1
        return arr
list = [2,3,4,5,4,3,6]
print(reverseArray(list))
# results = []

# def factorial(n):
#     if n == 0 or n == 1:
#         results.append(1)
#         return 1
#     else:
#         result = n * factorial(n-1)
#         results.append(result)
#         return result

# factorial(5)
# print(factorial(5))


# # results = []

# # def factorial(n):
# #     if n == 0 or n == 1:
# #         results.append(1)
# #         return 1
# #     else:
# #         result = n * factorial(n-1)
# #         results.append(result)
# # factorial(5)
# # print(results)
# # # def fact(n):
# # #     list= []
# # #     if n == 0:
# # #         return 1 
# # #     if  n*fact(n-1) <= n:
# # #         list.append(n*fact(n-1))
# # # print(fact(5))

# # # # def fun(n):
# # # #     if n == 0:
# # # #         return 1
# # # #     return n * fun(n-1)

# # # # print(fun(5))