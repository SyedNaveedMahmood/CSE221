def mergesort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  a1=mergesort(arr[0:mid])
  a2=mergesort(arr[mid:])
  sorted_arr=merge(a1,a2)
  return sorted_arr
def merge(a,b):
  i=0
  j=0
  l=[]
  while i<len(a) and j<len(b):
    if a[i]<=b[j]:
      l+=[a[i]]
      i+=1
    else:
      l+=[b[j]]
      j+=1
  if i<len(a):
    l+=a[i:]
  if j<len(b):
    l+=b[j:]
  return l
with open("input1.txt","r") as abc:
  var=abc.read().split('\n')[1:]
  v=open("output1.txt","w")
  arr=var[0].split(" ")
  for iter1 in range(len(arr)):
    arr[iter1]=int(arr[iter1])
  sorted_arr=mergesort(arr)
  for elem in sorted_arr:
    v.write(f"{elem} ")