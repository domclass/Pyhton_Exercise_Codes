# 斐波那契数列
# yield的用法
def fab2(max):
   n,a,b=0,0,1
   fab_list=[]
   for i in range(max):
       fab_list.append(b)
       yield fab_list
       a,b=b,a+b
      
for n in fab2(40):
    print ( n )


