# kwargs also called args or keyword args/argumetns 
# Example of Args 
# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(sum_of(4,5,6,7,8,9))

# Example of Kwargs
# def sum_of(**kwargs):
#     sum = 0
#     for x, m in kwargs.items():
#         sum += m
#     return sum

# print(round(sum_of(name = 15, Keyword = '123', names = 123.22), 2))

# Key Value Example of the Kwargs
def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    return 

kwargs(name = 'uzair' , roll_no = '15')