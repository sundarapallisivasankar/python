l=[]
n=int(input("Enter the size of  list"))
print("Enter the element into the list")
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
l.reverse()
print("reversed list:",l)
