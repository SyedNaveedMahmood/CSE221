with open("input1(b).txt","r") as abc:
  var=abc.read().split('\n')[1:]

  v=open("output1(b).txt","w")
  for i in range(0,len(var)-1):
    idx=len("calculate")
    exp=var[i][idx+1::1]
    if "+" in exp:
      operands=exp.split("+")
      result=int(operands[0])+int(operands[1])
    if "-" in exp:
      operands=exp.split("-")
      result=int(operands[0])-int(operands[1])
    if "/" in exp:
      operands=exp.split("/")
      result=int(operands[0])/int(operands[1])
    if "*" in exp:
      operands=exp.split("*")
      result=int(operands[0])*int(operands[1])
    v.write(f"The result of {exp} is {result} \n")
