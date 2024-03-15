with open("input1_2.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output1_2.txt","w")
    nodes=int(var[0][0])
    edges=int(var[0][2])
    dicta={}
    for i in range(nodes+1):
        dicta[i]=[]
    for i2 in range(1,len(var)-1):
        s_temp = var[i2].split(" ")
        n1=int(s_temp[0])
        n2=int(s_temp[1])
        w=int(s_temp[2])
        dicta[n1].append((w,n2))
    distance=[999999]*(nodes+1)
    source=int(var[len(var)-1])
    parent=[0]*(nodes+1)
    parent[source]=source
    def min_index(mini, subset):
        for index in range(len(subset)):
            if subset[index] == mini:
                return index
    def shortest_path(graph,src,dist,parent):
        queue=[]
        for elem in graph[src]:
            queue.append(elem)
        dist[src]=0
        prev=src
        while len(queue)!=0:
            min_val=min_index(min(queue),queue)
            start=queue.pop(min_val)
            for elem in graph[prev]:
                if dist[prev]+elem[0]<=dist[elem[1]]:
                    dist[elem[1]]=dist[prev]+elem[0]
                    queue.append((dist[elem[1]],elem[1]))
                    parent[elem[1]]=prev

            prev=start[1]
        return dist,parent
    result,par=shortest_path(dicta,source,distance,parent)
    print(result)
    # for iter2 in range(1,len(result)):
    #     if result[iter2]==999999:
    #         v.write("-1")
    #     else:
    #         v.write(str(result[iter2])+" ")