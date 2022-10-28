import math
a, b = input().split()
a = int(a)
b = int(b)
c = math.gcd(a, b)
d = int(a * b / c)
print("最大公约数是", c)
print("最小公倍数是", d)
