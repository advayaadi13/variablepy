lst = ['Mango','Watermelon','Apple','Pineapple','Orange']

print("Length of list: ", len(lst))
print("First Element of List: ", lst[0])
print("Last Element of List: ", lst[-1])

lst.append('Banana')
print("Updated List: ", lst)

lst.remove('Pineapple')
print("Updated List: ", lst)

lst.sort()
print("Sorted List: ", lst)

lst.pop(1)
print("Updated List: ", lst)

lst.reverse()
print("Reversed List: ", lst)

print("Multiplication on List: ", lst*2)

lst = lst[:4]
print("Sliced List: ", lst)

lst.clear()
print("Updated List: ", lst)
