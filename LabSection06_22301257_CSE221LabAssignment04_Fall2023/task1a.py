with open("input1a_1.txt","r") as abc:
  var=abc.read().split('\n')
  v=open("output1a_1.txt","w")
  temp=var[0].split(" ")
  ver=int(temp[0])
  edges=int(temp[1])
  multi_list=[]
  for i in range(ver+1):
    temp_list=[]
    for j in range(ver+1):
      temp_list.append(0)
    multi_list.append(temp_list)
  for k in range(1,len(var)):
    s_temp=var[k].split(" ")
    n1=int(s_temp[0])
    n2=int(s_temp[1])
    w=int(s_temp[2])
    multi_list[n1][n2]=w
for elem in multi_list:
  for elem2 in elem:
    v.write(str(elem2) + " ")
  v.write("\n")