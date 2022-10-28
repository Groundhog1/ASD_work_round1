from math import sqrt as s


def prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        print(n)
    else:
        if n < 2:
            return
        else:
            i = 2
            breaknum = int(s(n) + 1)
            while i < breaknum:
                if n % i == 0:
                    break
                i += 1
            if i == breaknum:
                print(n)


j = 1
while j < 1000:
    prime(j)
    j += 1
