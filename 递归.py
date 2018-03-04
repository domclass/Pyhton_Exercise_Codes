# 递归计算阶乘factorial
# 利用递归来做字符反转

def fact(n):
        if n==0:
            return 1
        else:
            return n*fact(n-1)
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]

print (reverse("Hello"))

