def merge_count(arr):
  n = len(arr)
  if n <= 1:
    return 0
  mid = n // 2
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  count1 = merge_count(left_arr) + merge_count(right_arr)
  iter1 =0
  iter2 =0
  iter3 = 0
  while iter1 < len(left_arr) and iter2 < len(right_arr):
    if left_arr[iter1] <= right_arr[iter2]:
      arr[iter3] = left_arr[iter1]
      iter1 += 1
      iter3 +=1
    else:
      arr[iter3] = right_arr[iter2]
      iter2 += 1
      count1 +=  len(left_arr) - iter1
      iter3 += 1
  while iter1 < len(left_arr):
    arr[iter3] = left_arr[iter1]
    iter1 += 1
    iter3 += 1
  while iter2 < len(right_arr):
    arr[iter3] = right_arr[iter2]
    iter2 += 1
    iter3 += 1
  return count1
with open("input3.txt","r") as abc:
  var=abc.read().split('\n')[1:]
  c=open("output3.txt","w")
  arr=var[0].split(" ")
  for iter1 in range(len(arr)):
    arr[iter1]=int(arr[iter1])
  count=merge_count(arr)
  c.write(f"{count}")