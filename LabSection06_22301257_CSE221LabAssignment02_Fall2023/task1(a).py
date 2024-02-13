with open("input1(a).txt","r") as abc:
  var=abc.read().split("\n")[0:]
  output=open("output1(a).txt", "w")
  length,target=var[0].split()
  digits=var[1].split()
  tar=int(target)
  flag=True
  for i in range(int(length)):
    for j in range(int(length)-1,i,-1):
      if int(digits[i])+int(digits[j])== tar :
        output.write(f"{i+1} {j+1}")
        flag=False
        break
    if flag==False:
      break
  if flag==True:
    output.write("IMPOSSIBLE")
