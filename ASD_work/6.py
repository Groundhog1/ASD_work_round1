lim = int(input("几个杨辉三角呀"))


def ziplus(xc):
    mylen = len(xc)
    i = 0
    out_list = [1]
    while i < mylen - 1:
        tmp = xc[i] + xc[i + 1]
        out_list.append(tmp)
        i += 1
    out_list.append(1)
    return out_list


a = [1]
j = 0
while j < lim:
    x = str(a)
    print(x.center(lim * 10))
    a = ziplus(a)
    j += 1
