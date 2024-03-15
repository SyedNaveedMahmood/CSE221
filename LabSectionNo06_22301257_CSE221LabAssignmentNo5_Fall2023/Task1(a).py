with open("input1(a)_3.txt","r") as abc:
    var=abc.read().split('\n')
    v=open("output1(a)_3.txt","w")
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
    visited=[False]*(courses+1)
    top_sort=[]
    def dfs(graph,start,visited,res):
        if visited[start]==False:
            visited[start]=True
            res.append(start)
            for connection in graph[start]:
                dfs(graph,connection,visited,res)
    dfs(dicta,start,visited,top_sort)
    for j in range(1,len(visited)):
        if visited[j]==False:
            dfs(dicta,j,visited,top_sort)
    flag=True
    for i in range(len(top_sort)):
        for elem in dicta[top_sort[i]]:
            for iter in range(i):
                if top_sort[iter] == elem:
                    flag = False
        for iter2 in range(i + 1, len(top_sort)):
            if top_sort[iter2] == top_sort[i]:
                flag = False
    if flag==True:
        for elem2 in top_sort:
            v.write(str(elem2)+" ")
    else:
        v.write("Impossible")

