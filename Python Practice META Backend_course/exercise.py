count = 0
num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for index, i in enumerate(num_list):
    print(i)
    
    if i > 45:
        print("Over 45")
    else:
        print("Under 45")
    
    if i == 36:
        print("Number Found at position: ", index)
    
    count += 1

print("Total count:", count)
