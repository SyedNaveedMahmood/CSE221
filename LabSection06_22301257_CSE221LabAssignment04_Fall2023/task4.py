with open("input4_1.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output4_1.txt","w")
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
    def bfs(graph,start,cities):
        flag=[False]*(cities+1)
        q=[]
        q.append(start)
        flag[start]=True
        flag1=True
        while len(q)!=0:
            current=q.pop(0)
            for connection in graph[current]:
                if flag[connection]==False:
                    q.append(connection)
                    flag[connection]=True
                if flag[connection]!=False:
                    for elem in graph[connection]:
                        if flag[elem] == True:
                            for elem2 in graph[elem]:
                                if flag[elem2]==True:
                                    flag1=False
        if flag1==True:
            v.write("NO")
        else:
            v.write("YES")
    bfs(dicta,start,cities)