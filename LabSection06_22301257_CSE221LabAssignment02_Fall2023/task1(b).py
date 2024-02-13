with open("input1(b).txt", "r") as abc:
  var=abc.read().split("\n")[0:]
  output=open("output1(b).txt", "w")
  length,target=var[0].split()
  digits=var[1].split()
  tar=int(target)
  flag=True
  i=0
  j=int(length)-1
  while i<j:
    if int(digits[i])+int(digits[j])== tar:
      output.write(f"{i+1} {j+1}")
      flag=False
      break
    if int(digits[i])+int(digits[j])>tar:
      j-=1
    if int(digits[i])+int(digits[j])<tar:
      i+=1
  if flag==True:
      output.write("IMPOSSIBLE")