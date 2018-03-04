# 九九乘法
# yield的用法
def table_9_9(max=9):
    n=1
    while n<=max:
        N=['{}*{}=={}'.format(i,n,i*n) for i in range(1,n+1)]
        n+=1
        yield N

T=table_9_9()
for t in T:
    print (t)
   