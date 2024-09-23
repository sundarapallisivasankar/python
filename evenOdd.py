l=[]
n=int(input("Enter the size of  list"))
print("Enter the elements into the list")
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
even=[]
odd=[]
for i in l:
	if (i%2==0):
		even.append(i)
	else:
		odd.append(i)
print(even)
print(odd)		

