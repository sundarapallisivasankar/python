"""#reversing a string
s  =input("Enter a string :")
print(s[::-1])
"""

#reversing string without slicing
""" s=input("Enter the string: ")
s1=""
for i in s:
	s1=i+s1
print(s1)
"""

#palindrome checking
"""s=input("Enter a string: ")
s1=s[::-1]
if s==s1:
	print("Given number is palindrome")
else:
	print("Not Palindrome")
"""

#length of string
"""s=input("Enter the string:")
count=0
for i in s:
	count=count+1
print(count)
"""
#counting vowels
"""s=input("Enter the string: ")
count=0
for i in s:
	if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
		count+=1 
print(count)
"""
#even length of words
"""str=input("Enter the string:")#.split()
for i in str.split():
	if len(i)%2==0:
		print(i)
"""





