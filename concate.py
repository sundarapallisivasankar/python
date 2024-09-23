#program to concatenate two list index wise
list1=["M","na","i","Abhi"]
list2=["y","me","s","Ram"]
list=[]
for i in range(min(len(list1),len(list2))):
	ele=list1[i]+list2[i]
	list.append(ele)
print(list)
