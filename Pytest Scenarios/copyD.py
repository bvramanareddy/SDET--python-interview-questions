import copy

list1= [1,2,3,4,5,"Ramana"]

new1= copy.deepcopy(list1)
new1[0] ='Reddy'
print(new1)
print(list1)
list1.append("ShallowCopy")
print(new1)


list2 = list1.copy()
print(list2)
list2[0]= "Rama"
print(list2)
print(list1)