list = [1,2,3,4,3,3,5,4,3,45,3,2,4,5,3,3,2,4]
dictionary = {}
for i in list:
    if i in dictionary:
        dictionary[i] +=1
    else:
        dictionary[i] = 1
for i in range(10):
    intt = input("Input Number to Check Occuruence: ")
    print(dictionary.get(int(intt,0)))
# #  Counting number occurence using hash table
# list = [1,2,3,4,3,3,5,4,3,45,3,2,4,5,3,3,2,4]
# length = max(list) + 1
# hash_list = [0] * length
# for i in list:
#     hash_list[i] += 1

# for i in range(10):
#     intt = input("Input Number to Check Occuruence: ")
#     print(hash_list[int(intt)])