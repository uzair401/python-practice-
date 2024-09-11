import random
f = open('names.txt' , 'r')
new_file = f.read()
new_file_list = new_file.split('\n')
f.close()
print(random.choice(new_file_list))