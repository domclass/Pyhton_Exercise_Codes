# for/while 中的else用法

for n in range(2,10):
    for x in range(2,n):   #range(2,2) 没有数。
        if n%x == 0:
            print(n," equals ",x,"*",n//x)
            break
    else:
        print(n,"is a prime number")

