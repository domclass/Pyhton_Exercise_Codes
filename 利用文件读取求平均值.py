# 哨兵循环求平均值
# 利用文件读取
# 循环嵌套

def main():
    fileName=input("Which file contains those numbers>>")
    infile=open(fileName,'r')
    sum=0.0
    count=0
    line=infile.readline()
    while line!='':
        for xStr in line.split(","):
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print("\nThe average of the numbers is: ", sum/count)

main()
