# 数据驱动的动态路径绘制

import turtle

def main():
    #设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)
    #设置画笔
    pen=turtle.Turtle()
    pen.color('green')  #不起作用的
    pen.width(5)
    pen.shape('turtle')
    pen.speed(2)

    #读取文件
    result=[]
    file=open('data.txt','r')
    for line in file:
        result.append(list(map(float,line.split(','))))
        #line.split(',')：按逗号分隔成数组
        # map：对参数2进行参数1操作（把每个数组里的str转成float）
        # list：把上面的结果导成一个list
        # append：把新生成的list加到result这个list后面（是加list，不是把每个float加进去）
    print(result)

    #动态绘制
    for i in range((len(result))):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)

if __name__=='__main__':    # 如果是按模块导入，则不会运行
    main()