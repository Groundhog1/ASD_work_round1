from school import *
import os

tmp = "1"
admin = "opqda"
while tmp != "password":
    admin = input("请输入账户名,输入qwq直接退出")
    if admin == "qwq":
        break
    tmp = input("请输入密码")
    if tmp != "password":
        print("密码错误")

c = []
for item in range(0, 6):
    c.append(str(item))

while admin != "qwq":
    menu()
    a = input("请输入数字")

    if a not in c:
        a = input("请重新输入")
    if a == "0":
        break
    a = int(a)
    switch(a)


os.system('pause')
