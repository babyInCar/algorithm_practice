"""
 密码合格性校验
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1≤n≤100

输入描述：
一组字符串。

输出描述：
如果符合要求输出：OK，否则输出NG

示例一
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出：
OK
NG
NG
OK

"""
def check(pw):
    if len(pw)<=8:
        return 0
    a,b,c,d = 0,0,0,0
    for s in pw:
        if s.isupper():
            a = 1
        elif s.islower():
            b = 1
        elif s.isdigit():
            c = 1
        else:
            d = 1
    if a+b+c+d < 3:
        return 0
    dc = {}
    for i in range(len(pw)-3):
        if pw[i:i+3] in dc.keys():
            return 0
        else:
            dc[pw[i:i+3]] = 1
    return 1

while 1:
    try:
        print('OK' if check(input()) else 'NG')
    except:
        break