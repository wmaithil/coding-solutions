n=int(raw_input()) 	#accept number of dict elements
dic={}	#initialise dictionary

#Inserting values in dictionary
for i in range(n):
	ip=[]
	ip=list(map(str, raw_input().split()))
	dic[ip[0]]=ip[1]

# issue continuous input from user
while(True):
	query=raw_input()
	if query not in dic:
		print("Not found")
	else:
		print("{0}={1}".format(query,dic[query]))
	



