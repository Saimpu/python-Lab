pali=input("enter the words")
r_pali=""
for i in pali:
	r_pali=i+r_pali
if(pali==r_pali):
	print("Palindrom")
else:
	print("not a Palindrom")
