with open("input4.txt", "r") as abc:
    var = abc.read().split("\n")[0:]
    n = int(var[0][0])
    m = int(var[0][2])
    output = open("output4.txt", "w")
    l = []
    for i in range(1, len(var)):
        l.append(var[i].split())


    def turn_into_int(arr):
        for elem in arr:
            for k in range(0, len(elem)):
                elem[k] = int(elem[k])
        return arr
    def bubbleSort(arr):
        flag = True
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j][1] > arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = False
            if flag == True:
                break
        return arr
    arr = turn_into_int(l)
    sorted_arr = bubbleSort(arr)
    people_list=[]
    for i in range(m):
        people_list.append([])
    for iter1 in range(n):
        minL = []
        min = 99999
        idx = -1
        for iter2 in range(m):
            if len(people_list[iter2])==0:
                people_list[iter2]+=[sorted_arr[iter1]]
                break
            elif sorted_arr[iter1][0]==people_list[iter2][-1][1]:
                people_list[iter2] += [sorted_arr[iter1]]
                break
            else:
                minL+=[sorted_arr[iter1][0]-people_list[iter2][-1][1]]
                if iter2==m-1:
                    for iter3 in range(len(minL)):
                        if minL[iter3] < min and minL[iter3]>-1:
                            min= minL[iter3]
                            idx=iter3
                    if minL[idx]>-1:
                        people_list[idx]+=[sorted_arr[iter1]]
                    break
    count=0
    for j in range(len(people_list)):
        count+=len(people_list[j])
    output.write(str(count))



