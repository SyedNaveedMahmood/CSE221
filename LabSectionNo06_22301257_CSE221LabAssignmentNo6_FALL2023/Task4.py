with open("input4_2.txt","r") as abc:
    output = open("output4_2.txt", "w")
    def disjoint_set(n1,n2):
            n1 = int(n1)
            n1 = int(n1)
            n2 = int(n2)
            u = find(n1)
            v = find(n2)
            if u > v:
                count = 0
                for i2 in range(len(parent)):
                    if parent[i2] == u:
                        parent[i2] = v
            elif u < v:
                count = 0
                for i2 in range(len(parent)):
                    if parent[i2] == v:
                        parent[i2] = u
    def find(r):
        if parent[r] == r:
            return r
        return find(parent[r])
    var=abc.read().split("\n")

    cities=int(var[0][0])
    roades=int(var[0][2])
    graph=[]
    for i2 in range(1,len(var)-1):
        s_temp = var[i2].split(" ")
        n1=int(s_temp[0])
        n2=int(s_temp[1])
        w=int(s_temp[2])
        graph.append((n1,n2,w))
    parent = [None] * (cities + 1)
    for i in range(cities + 1):
        parent[i] = i
    def last(n):
        return n[-1]
    sorted_w=sorted(graph,key=last)
    minimal_cost=0
    for elem in sorted_w:
        if parent[elem[0]]!=parent[elem[1]]:
            disjoint_set(elem[0],elem[1])
            minimal_cost+=elem[2]
    output.write((str(minimal_cost)))