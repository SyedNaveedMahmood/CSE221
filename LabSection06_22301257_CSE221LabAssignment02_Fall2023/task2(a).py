with open("input2(a).txt","r") as abc:
  var=abc.read().split("\n")[0:]
  output=open("output2(a).txt","w")
  def turn(arr):
    for i in range(len(arr)):
      arr[i]=int(arr[i])
    return arr
  s1=var[1].split()
  s2=var[3].split()
  s1_int=turn(s1)
  s2_int=turn(s2)
  new=s1+s2
  sorted_arr=sorted(new)
  for elem in sorted_arr:
    output.write("".join(str(elem)+" "))