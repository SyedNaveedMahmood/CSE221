def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def quickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)
        return arr
with open("input5.txt","r") as abc:
  var=abc.read().split('\n')[1:]
  c=open("output5.txt","w")
  arr=var[0].split(" ")
  for iter1 in range(len(arr)):
    arr[iter1]=int(arr[iter1])
  sorted_arr=quickSort(arr,0,len(arr)-1)
  for elem in sorted_arr:
    c.write("".join(str(elem)+" "))
