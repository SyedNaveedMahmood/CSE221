with open("input1(b)_1.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output1(b)_1.txt","w")
    temp=var[0].split(" ")
    courses=int(temp[0])
    preq=int(temp[1])
    dicta = {}
    start=int(var[1][0])
    for i in range(courses + 1):
        dicta[i] = []
    for k in range(1, len(var)):
        s_temp = var[k].split(" ")
        n1 = int(s_temp[0])
        n2 = int(s_temp[1])
        dicta[n1].append(n2)
    in_degree = [0] * (courses+1)
    for i in dicta:
        for j in dicta[i]:
            in_degree[j] += 1
    in_degree[0]=9999
    top_sort=[]
    def bfs(graph,in_deg,top_sort,courses):
        queue = []
        for i in range(courses):
            if in_deg[i] == 0:
                queue.append(i)
        while queue:
            start = queue.pop(0)
            top_sort.append(start)
            for i in graph[start]:
                in_deg[i] -= 1
                if in_deg[i] == 0:
                    queue.append(i)
    bfs(dicta,in_degree,top_sort,courses)

    if len(top_sort)!=courses:
        v.write("Impossible")
    else:
        for elem2 in top_sort:
            v.write(str(elem2)+" ")