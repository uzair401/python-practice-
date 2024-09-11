# Dictionary
# Key Value pairs
# you can access the item using the key 
# Dictionaty syntax
dictionaty = {1: 'tea', 2: True,"name": "uzair", "location": "unknown"}
print(dictionaty["name"])
dictionaty[1] = 'Black Tea'
print(dictionaty[1])

# can delete item using del Keyword

# iteration Methods 
# 1: can access using direct function keyword and the Iteration or loop methods. but using the for loop. the 
# dictionary will only display the keys but if you wanna access the data then you have to use the .item() functoin
print(dictionaty)
# 2 : access using key 
print(dictionaty['name'])
# 3rd is .items() and .values() Function 
# Updation is as sample as updating the other values using indexes but here you will update using keys
#  Duplication of keys are not allowed. it will override the previous key with the new value.
