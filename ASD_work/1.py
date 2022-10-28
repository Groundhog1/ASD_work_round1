a = input("What's your name")
b = input("please input your number")
c = input("your class?")
d = input("你的性别")

while a == "":
    a = input("You need tell me your name!!!")
while c not in ['1', '2', '3', '4', '5', '6']:
    c = input("your class is wrong, input again")

while d not in ["男", "女"]:
    d = input("请输入合法的性别")

print("你是", a, "，学号为", b, "，是来自", c, "班的", d, "生")
