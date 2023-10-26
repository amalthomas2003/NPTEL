def expanding(l):
    abs_diff=0
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])>abs_diff:
            abs_diff=abs(l[i]-l[i+1])
        else:
            return False
    return True
#print(expanding([1,2,3]))

##################################################

def sumsquare(l):
    list1=[0,0]
    for i in l:
        if i%2==0:
            list1[1]+=pow(i,2)
        else:
            list1[0]+=pow(i,2)
    return list1
#print(sumsquare([-1,-2,3,7]))


################################################

def transpose(m):
    list2=[]
    
    for i in range(len(m[0])):
        list1=[]
        for j in range(len(m)):
            list1.append(m[j][i])
        list2.append(list1)
    return(list2)
#print(transpose([[3]]))
            
            


            
###################

import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "expanding":
  arg = parse(farg)
  print(expanding(arg))

if fname == "sumsquare":
  arg = parse(farg)
  print(sumsquare(arg))

if fname == "transpose":
  arg = parse(farg)
  savearg = arg
  ans = transpose(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")