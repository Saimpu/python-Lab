n=int(input("enter the values"))
f1=0
f2=1
print("0")
print("1")
for i in range(n+1):
	next=f1+f2
	print(next)
	f1=f2
	f2=next

