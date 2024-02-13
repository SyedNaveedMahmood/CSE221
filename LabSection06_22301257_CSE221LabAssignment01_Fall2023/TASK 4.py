
with open("input4.txt", "r") as abc:
    output = open("output4.txt", "w")
    def time_converter(t):
        li=t.split(":")
        hours=int(li[0])
        minutes = int(li[1])
        total = (hours*60)+minutes
        return total
    l = abc.read().split("\n")[1:-1]
    output = open("output4.txt", "w")
    for i in range(len(l) - 1):
        for j in range(len(l)-i-1):
            l1 = l[j].split(" ")
            name = l1[0]
            time = l1[6]
            time_min = time_converter(time)
            l2 = l[j+1].split(" ")
            name2 = l2[0]
            time2 = l2[6]
            t2=time_converter(time2)
            if name>name2:
                l[j],l[j+1]=l[j+1],l[j]
            if name==name2:
                if time_min<t2:
                    l[j], l[j+1] = l[j+1], l[j]
    for elem in l:
        output.write(f"{elem} \n")
