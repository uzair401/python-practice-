# List Comprehension.
# data = [10,20,30,40,50]

# new_data = [round(x/5) for x in data]
# print(new_data)
# new_data = data
# for x in data:
#     print(x , end = " ")

# Dictionaries Comprehensions 
nums = [923489453401, 923429385688, 923075005891]
names = ['uzair', 'aqib', 'uzair_jazz']

nameAndNums = {key:value for (key,value) in zip(names, nums)}

print("List To Dict Example is = ", nameAndNums)