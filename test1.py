n=int(input("enter no = "))
result=""
for i in range(1,n+1):
	for j in range(1,2*i):
		if j%2==0:
			result=result+"*"
		else:
			result=result+str(i)
	result=result+"\n"
for i in range(n,0,-1):
	for j in range(1,2*i):
		if j%2==0:
			result=result+"*"
		else:
			result=result+str(i)
	result=result+"\n"
print(result)