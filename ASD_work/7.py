a = input("字符串")
a = str.lower(a)
b = input("单词")
c = a.split()
count = 0
for x in c:
    if x == b:
        count += 1

print(count)
