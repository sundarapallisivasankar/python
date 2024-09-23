#program for finding sum and avg using list
l=[]
n=int (input("Enter  the size of  list"))
for i in range(n):
	ele=int(input("enter the element"))
	l.append(ele)
print(l)
s=sum(l);
print("Sum of numbers in list:",s)
avg=s/n
print("Average of numbers: ",avg)
