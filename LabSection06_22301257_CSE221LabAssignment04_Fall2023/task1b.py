with open("input1b_1.txt","r") as abc:
  var=abc.read().split('\n')
  output=open("output1b_1.txt","w")
  temp=var[0].split(" ")
  ver=int(temp[0])
  edges=int(temp[1])
  dicta={}
  for i in range(ver+1):
    dicta[i]=""
  for k in range(1, len(var)):
    s_temp = var[k].split(" ")
    n1 = int(s_temp[0])
    n2 = int(s_temp[1])
    w = int(s_temp[2])
    dicta[n1]+=" ("+str(n2)+","+str(w)+")"
  for k,v in dicta.items():
    output.write(str(k)+":"+str(v)+"\n")