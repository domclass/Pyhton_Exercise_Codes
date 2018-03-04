# 文件的读取输出

infile=open("test.txt",'r')
outfile=open('test3.txt','w')
for i in range(5):
    line=infile.readline()
    # print(line[:-1])
    outfile.write(line[:-1])  #就少回车了，果然屏幕输出和文件不一样
infile.close()
outfile.close()