# Sets e.g
set = {1,2,3,4,5}
# Sets are like mathematical sets. sets cannot print duplicate values. e.g
set_1 = {1,2,3,4,5,5,6,6}
print(set_1)
# you can add values to set using .add() funciton.
# can remove the values using discard and remove funciton.
# sets are unorder and oyu cannot print the values of set using the iteration or loops
# you can use the intersection(), union(), symmetric_difference() and difference() function to perform several tasks
# union
print(set.union(set_1))
# intersetion
print(set.intersection(set_1))
# difference 
print(set.difference(set_1))
# symetrical values means values which are similar in both sets.
print(set.symmetric_difference(set_1))