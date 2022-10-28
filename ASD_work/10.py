# -*- coding：utf-8 -*-
import os

friends = {
    'jiaLiang': 23,
    'wangChen': 24,
    'jiaMing': 22,
    'wangJie': 22,
    'yuQing': 24,
    'wenZhen': 23,
    'haoNan': 25,
    'luYi': 23,
    'boWen': 23
}

for k, v in friends.items():
    print(k.ljust(12), v)

os.system('pause')

for k in friends:
    print(k)

os.system('pause')

a = list(friends)
b = sorted(a)
for kplus in b:
    print(kplus)

os.system('pause')

for v in friends.values():
    print(v)

list_v = list(friends.values())

max_num = max(list_v)
min_num = min(list_v)

print(f"Your friends' age is between %d and %d" % (min_num, max_num))

os.system('pause')

list_set = set(friends.values())
for j in list_set:
    print(j)

os.system('pause')

friends['xiaomi'] = 18

xiaoxuemei = {}
for k, v in friends.items():
    if v < 23:
        xiaoxuemei[k] = v
friends = xiaoxuemei

for k, v in friends.items():
    print(k.ljust(12), v)

os.system('pause')
