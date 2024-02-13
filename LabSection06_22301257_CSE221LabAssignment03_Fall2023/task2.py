def divide(arr):
  if len(arr)<=1:
    return arr[0]
  mid=len(arr)//2
  a1=divide(arr[0:mid])
  a2=divide(arr[mid:])
  if a1>=a2:
    return a1
  else:
    return a2
with open("input2.txt","r") as abc:
  var=abc.read().split('\n')[1:]
  c=open("output2.txt","w")
  arr=var[0].split(" ")
  for iter1 in range(len(arr)):
    arr[iter1]=int(arr[iter1])
  divide=divide(arr)
  c.write(f"{divide}")

#("The time complexity of  the code is O(n log n)")