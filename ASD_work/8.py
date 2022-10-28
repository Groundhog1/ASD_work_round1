from math import sqrt as s


def prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 1
    else:
        if n < 2:
            return 0
        else:
            i = 2
            breaknum = int(s(n) + 1)
            while i < breaknum:
                if n % i == 0:
                    return 0
                i += 1
            if i == breaknum:
                return 1


strnum = input("请输入待测数据")
strnum_opp = list(reversed(strnum))
c = list(strnum)
if strnum_opp == c and prime(int(strnum)) == 1:
    print("YES")
else:
    print("NO")
