import os


class Student:
    def __init__(self):
        self.stulist = []
        self.stunum = 0

    def addstu(self, number, name, age, gen, grade, leader):
        for x in self.stulist:
            if name == x:
                print(name, "is already in list")
        self.stunum += 1
        self.stulist.append([number, name, age, gen, grade, leader])

    def killstu_2(self, name):
        for x in self.stulist:
            if name in x:
                print("删除", name, "的信息")
                self.stulist.remove(x)
                self.stunum -= 1
                return True
        print(name, "不在列表中")
        return False

    def search_1(self, name):
        for x in self.stulist:
            if name in x:
                print(name, "在列表中")
                print("学号：", x[0], "姓名", x[1], "年龄：", x[2], "性别：", x[3], "年级", x[4], "班主任", x[5])
                return True
        print(name, "不在列表中")
        return False

    def outprint(self):
        print(s.stunum)
        for x in self.stulist:
            print(x)


s = Student()


def menu():
    # 输出菜单
    print('''
    ------------------学生信息管理系统-----------------
    |                                                |
    |====================功能菜单=====================|
    |                                                |
    |                                                |
    |     1 录入学生信息                               |
    |     2 查找学生信息                               | 
    |     3 删除学生信息                               |
    |     4 修改学生信息                               |
    |     5 显示学生全部信息                            |
    |     0 退出系统                                   |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |===============================================  |
    |                                                 |
    |------------------------------------------------ |
    ''')


def switch(y):
    if y == 1:
        tname = input("学生的姓名")
        tshu = input("请输入学号")
        if tshu in s.stulist:
            return False
        tgen = input("请输入性别")
        if tgen not in ["男", "女"]:
            return False

        told = input("年龄")
        grade = input("请输入年级")
        lead = input("请输入班主任")

        s.addstu(tshu, tname, told, tgen, grade, lead)

    if y == 2:
        tname = input("学生的姓名")
        s.search_1(tname)

    if y == 3:
        tname = input("学生的姓名")
        s.search_1("tname")
        pppp = input("输入0确认继续，其他任意字符退出")
        if pppp == "0":
            s.killstu_2(tname)

    if y == 4:
        tname = input("学生的姓名")
        s.search_1("tname")
        pppp = input("输入0确认继续，其他任意字符退出")
        if pppp == "0":
            s.killstu_2(tname)
            tname = input("学生的姓名")
            tshu = input("请输入学号")
            tgen = input("请输入性别")
            told = input("年龄")
            grade = input("请输入年级")
            lead = input("请输入班主任")

            s.addstu(tshu, tname, told, tgen, grade, lead)

    if y == 5:
        s.outprint()

    os.system('pause')
