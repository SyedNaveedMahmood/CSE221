with open("input2(b).txt", "r") as abc:
    def turn(arr):
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr
    def merge(a, b):
        i = 0
        j = 0
        l = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                l += [a[i]]
                i += 1
            else:
                l += [b[j]]
                j += 1
        if i < len(a):
            l += a[i:]
        if j < len(b):
            l += b[j:]
        return l
    var = abc.read().split("\n")[0:]
    output = open("output2(b).txt", "w")
    s1 = var[1].split()
    arr1 = turn(s1)
    s2 = var[3].split()
    arr2 = turn(s2)
    sorted_arr = merge(arr1, arr2)
    for elem in sorted_arr:
        output.write("".join(str(elem) + " "))

