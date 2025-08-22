n=input("enter the string")
count=0
h=''
for i in n:
	count+=1
count+=1
while(count!=0):
	h=n[::-1]
	count-=1
if(n==h):
	print("Palindrom")
else:
	print("not a palindrom")
	
	
