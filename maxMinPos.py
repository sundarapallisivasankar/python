#program for finding max,min position of element list
l=[]
n=int(input("Enter the size of  list"))
print("Enter the elements into the list")
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
maxpos=l.index(max(l))
minpos=l.index(min(l))
print("index of  max elemnt",maxpos) 
print("index of  min element",minpos)
