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

def max_sum(arr):
  squared_val = []
  for idx in range(len(arr)):
    val = arr[idx]
    squared_val.append((val ** 2, idx))
  squared_val = mergesort(squared_val)
  i, j = 0, len(arr) - 1
  max_val = 0
  while i < j:
    if squared_val[j][1] <= i:
      j -= 1
    sum = arr[i] + squared_val[j][0]
    max_val = max(max_val, sum)
    i += 1
  return max_val
with open("input4.txt","r") as abc:
  var=abc.read().split('\n')[1:]
  c=open("output4.txt","w")
  arr=var[0].split(" ")
  for iter1 in range(len(arr)):
    arr[iter1]=int(arr[iter1])
  maximum=max_sum(arr)
  c.write(f"{maximum}")