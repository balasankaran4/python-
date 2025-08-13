List=[10,20,30,40,50]
print("List befor changes:",List)
index=2
element=30
List.insert(index,element)
print("List after insertion :",List)
index=3
remove=List.pop(index)
print("List after removal:",List)
print("Removed Element:",remove)