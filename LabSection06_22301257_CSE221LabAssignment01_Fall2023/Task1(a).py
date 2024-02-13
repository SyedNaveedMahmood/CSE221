with open("input1(a).txt","r") as abc:
  var = abc.readlines()
  v=open("output1(a).txt","w")
  for i in range(1,len(var)):
    if int(var[i])%2==0:
      v.write(f"{int(var[i])} is an Even number \n")
    else:
      v.write(f"{int(var[i])} is an Odd number \n")
