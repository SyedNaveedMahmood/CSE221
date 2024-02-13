with open("input3.txt", "r") as abc:
    var = abc.read().split("\n")[0:]
    output = open("output3.txt", "w")
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
    fin = []
    fin.append(sorted_arr[0])
    count = 1
    ref = sorted_arr[0][1]
    for j in range(len(sorted_arr) - 1):
        if (ref <= sorted_arr[j + 1][0]):
            fin.append(sorted_arr[j + 1])
            ref = sorted_arr[j + 1][1]
            count += 1
    output.write(str(count))
    output.write("\n")
    for elem in fin:
        for elem2 in elem:
            output.write(str(elem2) + " ")
        output.write("\n")