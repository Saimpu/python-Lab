even=input("Enter the Sentence")
evenS=even.split()
a=''
for i in evenS:
	if(len(i)%2==0):
		a=a+i
print(a)

