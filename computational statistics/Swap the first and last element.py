List=[10,20,30,40.45,26]
print("Original List:",List)
if len(List) >=2:
    List[0],List[-1]=List[-1],List[0]
print("List after Interchanging first and last element :",List)    