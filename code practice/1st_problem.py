def reverse( x):
        sign = -1 if x < 0 else 1
        print(x)
        if x < 0:
              x = -x 
        print(x)
        
        reversed_number = 0 
        while x > 0:
            num = int(x % 10)
            reversed_number = int(reversed_number *10)+ num
            x = x // 10

            if reversed_number * sign > 2**31 - 1 or reversed_number * sign < -2**31:
                return 0
        return reversed_number * sign
print(reverse(1534236469))
# def findSingle(n, arr):
#     count_dict = {}
    
#     for num in arr:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
    
#     for key, value in count_dict.items():
#         if value == 1:
#             return key

# array = [1,2,3,5,3,2,1,4,5,6,6]
# print(findSingle(11, array))