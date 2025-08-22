n=int(input("enter the num"))
reverse=0
rev=""
while(n>0):
	reverse=n%10
	rev=rev+str(reverse)
	n=n//10
print(rev)
	
