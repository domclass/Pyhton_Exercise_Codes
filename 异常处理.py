# 将容易出现异常的程序放到try：里面。
# 这样来处理异常的出现
try:
    f=file('non-exist.txt')
    print ('File opened')
    f.close()
except:
    print ('File not exists')
print ('Done')
