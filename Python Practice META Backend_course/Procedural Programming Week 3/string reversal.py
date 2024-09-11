# def reverse(input_str):
#     new_str = ""
#     for item, x in enumerate(input_str):
#         new_str += input_str[len(input_str) - item - 1]

#     return new_str

# print(reverse('name'))

name = 'uzair'
reverseOfName = name[:: -1]
print(reverseOfName)