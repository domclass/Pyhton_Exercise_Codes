# 哨兵循环
# 求平均数，但是不限制输入数据的个数

def main():
    sum=0.0
    count=0
    xStr=input("Enter a number (<Enter> to quit)>> ")
    while xStr != "":
        sum=sum+eval(xStr)
        count=count+1
        xStr=input("Enter a number (<Enter> to quit)>> ")
    print("\nThe average of the numbers is: ", sum/count)

main()

