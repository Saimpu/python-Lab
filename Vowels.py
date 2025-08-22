vow=input("enter the Word with or without vowels")
count=0
for i in vow:
	if(i=='i' or i=='I'):
		count+=1
	elif(i=='O' or i=="o"):
		count+=1
	elif(i=='e' or i=='E'):
		count+=1
	elif(i=='u' or i=='U'):
		count+=1
	elif(i=='a' or i=='A'):
		count+=1
print(f"{count} Vowels in the give word")
