# 输入1-7，返回星期一-星期日

week="MonTueWedThuFriSatSun"
n=input("请输入数字（1-7）：")
pos=(int(n)-1)*3
print("对应星期的简写是："+week[pos:pos+3]+".")