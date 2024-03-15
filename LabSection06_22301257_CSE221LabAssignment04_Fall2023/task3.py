with open("input3_1.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output3_1.txt","w")
    temp=var[0].split(" ")
    cities=int(temp[0])
    roads=int(temp[1])
    dicta = {}
    start=int(var[1][0])

    for i in range(cities + 1):
        dicta[i] = []
    for k in range(1, len(var)):
        s_temp = var[k].split(" ")
        n1 = int(s_temp[0])
        n2 = int(s_temp[1])
        dicta[n1].append(n2)
        dicta[n2].append(n1)
    visited=[]
    def dfs(graph,start,visited):
        if start not in visited:
            v.write(str(start)+" ")
            visited.append(start)
            for connection in graph[start]:
                dfs(graph,connection,visited)
    dfs(dicta,start,visited)