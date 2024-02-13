def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def kthSmallest(arr, left, right, k):
    if (k > 0 and k <= right - left + 1):
        index = partition(arr, left, right)
        if index - left > k - 1:
            return kthSmallest(arr, left, index - 1, k)
        if index - left == k - 1:
            return arr[index]
        return kthSmallest(arr, index + 1, right,k - index + left - 1)
    return -1
with open("input6.txt","r") as abc:
      var=abc.read().split('\n')[1:]
      c=open("output6.txt","w")
      arr = var[0].split(" ")
      for iter1 in range(len(arr)):
          arr[iter1]=int(arr[iter1])
      t=int(var[1])
      iter3=2
      answer=[]
      for iter2 in range(t):
          k=int(var[iter3])
          answer.append(str(kthSmallest(arr, 0, len(arr) - 1,k)))
          iter3+=1
      for elem in answer:
          for elem2 in elem:
              c.write(str(elem2) + "")
          c.write("\n")