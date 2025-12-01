my_set = {1,2,2,3,4,4,4}
print("Set: ", my_set)

my_set.add(5)
print("Updated Set:", my_set)

set1 = my_set
set2 = {2,4,4,6}

print("\nSet 1", set1)
print("Set 2:", set2)
print("Difference")
print(set1.difference(set2))
print("Symmeteric Difference")
print(set1.symmetric_difference(set2))

setc1 = {"green", "blue"}
setc2 = {"blue", 'yellow'}
print("Original Sets: ")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)

setx1 = {"green", "blue"}
setx2 = {"blue", 'yellow'}
print("Original Sets: ")
print(setx1)
print(setx2)
setx = setx1.intersection(setx2)
print("\nIntersection of above sets:")
print(setx)