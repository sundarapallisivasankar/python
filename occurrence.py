l=[]
n=int(input("Enter the size of  list"))
print("Enter the elements into the list")
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
a=int(input("Enter the element to remove: "))
l.remove(a)
print(l)
