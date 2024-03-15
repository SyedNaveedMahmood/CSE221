with open("input3_2.txt","r") as abc:
	var=abc.read().split("\n")
	people,queries=(var[0].split(" "))
	people=int(people)
	queries=int(queries)
	parent=[None]*(people+1)
	output=open("output3_2.txt","w")
	for i in range(people+1):
		parent[i]=i
	def find(r):
		if parent[r]==r:
			return r
		return find(parent[r])
	for i1 in range(1,queries+1):
		n1,n2=var[i1].split(" ")
		n1=int(n1)
		n1=int(n1)
		n2=int(n2)
		u = find(n1)
		v = find(n2)
		if u>v:
			count = 0
			for i2 in range(len(parent)):
				if parent[i2]==u:
					parent[i2]=v
			count=0
			for elem in parent:
				if elem==v:
					count+=1
		elif u<v:
			count = 0
			for i2 in range(len(parent)):
				if parent[i2]==v:
					parent[i2]=u
			count=0
			for elem in parent:
				if elem==u:
					count+=1
		elif u==v:
			count=0
			for elem in parent:
				if elem == parent[n1]:
					count += 1
		output.write(str(count)+"\n")