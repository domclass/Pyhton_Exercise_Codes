# 文件拷贝

def main():
    #用户输入文件名
    f1=input("Enter a source file: ").strip()  #去掉首尾的空格
    f2=input("Enter a output file: ").strip()

    # 打开文件
    infile=open(f1,'r')
    outfile=open(f2,'w')

    #拷贝文件
    countLines=countChars=0
    for line in infile:
        countLines=countLines+1
        countChars=countChars+len(line)
        outfile.write(line)
    print(countLines,' lines end ',countChars,' chars copied ')

    infile.close()
    outfile.close()

main()

