with open("input2.txt","r") as abc:
  l=abc.read()[1:].split()
  for j in range(len(l)):
    l[j]=int(l[j])
  v=open("output2.txt","w")
  def bubbleSort(arr):
    flag=True
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=False
        if flag==True:
          break
    return arr
  arr=bubbleSort(l)
  s=str(arr)
  v.write("".join(s))
#EXPLAINATION:
##In order to make it O(n) for the best case scenerio I had to make sure that the loop ends after checking
# if the array is sorted from the start. So I used flag to make sure that if no swap has happened in
# the first iteration then we can say that the array is already sorted hence the loop will break and the array will be returned