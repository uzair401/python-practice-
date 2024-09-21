# Using Hashing technique with hash maps / Dictionary 
string = "hello this is uzzzzair A}"
# string = string.replace(" ", "") // We Don't need to remove spaces because space has its own ascii value
dict = {}
for i in string:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
print(dict)

def count(a):
    return dict[a]
print(count(' '))
# print(count(''))
# counting string charachter occurence using hash table


# string = "hello this is uzzzzair A }"
# # string = string.replace(" ", "") // We Don't need to remove spaces because space has its own ascii value
# hash = [0] * 256
# for i in string:
#     # print(ord(i)-ord('a'))
#     hash[ord(i)] += 1

# def count(a):
#     for i in hash:
#         return hash[ord(a)]
    
# print(count(''))
# # counting string charachter occurence using hash table

# string = "hello this is uzzzzair"
# string = string.replace(" ", "")
# hash = [0] * 26
# for i in string:
#     # print(ord(i)-ord('a'))
#     hash[ord(i) - ord('a')] += 1

# def count(a):
#     for i in hash:
#         return hash[ord(a) - ord('a')]
    
# print(count('z'))