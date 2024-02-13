with open("input3.txt", "r") as abc:
    def selection_sorting(arr):
        for i in range(len(arr)):
            mins = int(arr[i])
            for j in range(i + 1, len(arr)):
                comp = int(arr[j])
                if comp >= mins:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    l = abc.read().split("\n")
    output = open("output3.txt", "w")
    l_id = (l[1].split(" "))
    l_num = l[2].split(" ")
    d = {}
    i = 0
    while i < len(l_id):
        d[l_id[i]] = int(l_num[i])
        i += 1
    sorted_arr = selection_sorting(l_num)
    sorted_d = dict(sorted(d.items()))
    j=0
    while j<len(sorted_arr):
        for k,v in sorted_d.items():
            if int(v) == int(sorted_arr[j]):
                output.write(f"ID: {k} Mark: {v} \n")
                sorted_d.pop(k)
                break
        j += 1