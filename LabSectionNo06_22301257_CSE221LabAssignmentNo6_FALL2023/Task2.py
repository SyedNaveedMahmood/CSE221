with open("input2_3.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output2_3.txt","w")
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
    distance1=[999999]*(nodes+1)
    distance2 = [999999] * (nodes + 1)
    sources=(var[len(var)-1].split(" "))
    src1,src2=int(sources[0]),int(sources[1])
    def min_index(mini, subset):
        for index in range(len(subset)):
            if subset[index] == mini:
                return index
    def shortest_path(graph,src,dist):
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
            prev=start[1]
        return dist
    result1=shortest_path(dicta,src1,distance1)
    result2 = shortest_path(dicta, src2, distance2)
    i=0
    sum_arr=[]
    while i!=len(result1):
        sum_arr.append(max(result1[i],result2[i]))
        i+=1
    time=min(sum_arr)
    node=sum_arr.index(time)
    if time<999999:
        v.write(f"Time {time} \n")
        v.write(f"Node {node} ")
    else:
        v.write("Impossible")