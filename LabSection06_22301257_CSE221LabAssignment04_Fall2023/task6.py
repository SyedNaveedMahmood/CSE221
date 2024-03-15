with (open("input6_1.txt","r") as abc):
    var=abc.read().split('\n')
    v=open("output6_1.txt","w")
    temp=var[0].split(" ")
    row=int(temp[0])
    col=int(temp[1])
    multi_list=[]
    for i in range(row):
        temp_list=[]
        for j in range(col):
          temp_list.append(0)
        multi_list.append(temp_list)
    iter=1
    for i in range(row):
        for j in range(col):
            multi_list[i][j]=var[iter][j]
        iter+=1
    def bfs(multi_list,x,y,block="#"):
        r=len(multi_list)
        c=len(multi_list[0])
        count = 0
        if multi_list[x][y]==block:
            return count
        q=[]
        q.append((x,y))
        while len(q)>0:
            x,y=q.pop(0)
            if x<0 or x>=r:
                continue
            if y<0 or y>=c:
                continue
            if multi_list[x][y]==block:
                continue
            else:
                if multi_list[x][y]=="D":
                    count+=1
                multi_list[x][y]=block
                q.append((x+1,y))
                q.append((x-1,y))
                q.append((x,y+1))
                q.append((x,y-1))
        return (count)
    def flood_fill(multi_list):
        max_l=[0]
        for i1 in range(row):
            for j1 in range(col):
                total=0
                if multi_list[i1][j1]==".":
                    total+=bfs(multi_list,i1,j1)
                    max_l.append(total)
        return max(max_l)
    max_d=flood_fill(multi_list)
    v.write(str(max_d))
