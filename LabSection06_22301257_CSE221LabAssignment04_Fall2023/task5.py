with open("input5_5.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output5_5.txt","w")
    temp=var[0].split(" ")
    cities=int(temp[0])
    roads=int(temp[1])
    destination=int(temp[2])
    dicta = {}
    start=1

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
                    q.append(connection)
                    distance[connection]=distance[current]+1
                    prev_node[connection]=current
        v.write("time :"+str(distance[destination])+"\n")
        shortest_path=[]
        back=destination
        while back!=None:
            shortest_path.append(back)
            back=prev_node[back]
        v.write(f"Shortest Path : ")
        for iter2 in range(len(shortest_path)-1,-1,-1):
            v.write(str(shortest_path[iter2])+" ")
    bfs(dicta,start,cities,destination)