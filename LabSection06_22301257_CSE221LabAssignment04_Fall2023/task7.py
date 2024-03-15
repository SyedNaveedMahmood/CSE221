with open("input7_1.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output7_1.txt","w")
    temp=var[0].split(" ")
    cities=int(var[0])
    dicta={}
    for i in range(cities + 1):
        dicta[i] = []
    for k in range(1, len(var)):
        s_temp = var[k].split(" ")
        n1 = int(s_temp[0])
        n2 = int(s_temp[1])
        dicta[n1].append(n2)
        dicta[n2].append(n1)
    def bfs(graph,start,cities,destination):
        flag=[False]*(cities+1)
        distance=[99999999]*(cities+1)
        prev_node=[None]*(cities+1)
        distance[start]=0
        q=[]
        q.append(start)
        flag[start]=True
        while len(q)!=0:
            current=q.pop(0)
            for connection in graph[current]:
                if distance[connection]>distance[current]+1:
                    distance[connection]=distance[current]+1
                    prev_node[connection]=current
                    q.append(connection)
        shortest_path=[]
        back=destination
        while back!=None:
            shortest_path.append(back)
            back=prev_node[back]
        return len(shortest_path)
    dict_paths={}
    for iter2 in range(1,cities+1):
        for iter3 in range(1,cities+1):
            dict_paths[bfs(dicta,iter2,cities,iter3)]=str(iter3)+" "+str(iter2)
    maxi=max(dict_paths)
    v.write(dict_paths[maxi])