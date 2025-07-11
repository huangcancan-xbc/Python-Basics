import sys
import os

# 使用列表表示所有的学生
students = []

def main():
    """程序的入口函数"""
    load()  # 程序启动时加载存档

    while True:
        choice = menu()

        if choice == 0:
            sys.exit()
        elif choice == 1:
            insert()
        elif choice == 2:
            show()
        elif choice == 3:
            find()
        elif choice == 4:
            delete()
        else:
            print('无效输入! 请重新输入!')

def menu():
    """显示程序菜单"""
    print("\n1. 新增学生")
    print("2. 显示所有同学信息")
    print("3. 根据名字查找学生信息")
    print("4. 删除学生信息")
    print("0. 退出程序")

    choice = input("请输入您的选择: ")
    return int(choice)

def insert():
    """新增学生"""
    print("[新增学生] 开始!")
    studentId = input("请输入学生的学号: ")
    name = input("请输入学生的姓名: ")
    gender = input("请输入学生的性别(男/女): ")

    if gender not in ('男', '女'):
        print("性别不符合要求! 请重新输入")
        return

    className = input("请输入学生的班级: ")

    # 使用一个字典表示学生信息
    student = {
        "studentId": studentId,
        "name": name,
        "gender": gender,
        "className": className
    }

    # 把字典添加到学生列表中
    global students
    students.append(student)
    print("[新增学生] 完毕!")
    save()  # 新增学生后自动存档


def show():
    """显示学生"""
    print("[显示学生] 开始!")
    for s in students:
        print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
    print(f"[显示学生] 完毕! 共显示了 {len(students)} 条记录!")


def find():
    """查找学生"""
    print("[查找学生] 开始!")
    name = input("请输入要查找的同学姓名: ")
    count = 0

    for s in students:
        if name == s['name']:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
            count += 1

    print(f"[查找学生] 完毕! 共查找到 {count} 条记录!")


def delete():
    """删除学生"""
    print("[删除学生] 开始!")
    studentId = input("请输入要删除的同学学号: ")
    count = 0

    # 创建列表副本用于遍历，避免修改原列表时出现问题
    for s in students[:]:
        if studentId == s['studentId']:
            print(f"删除 {s['name']} 同学信息")
            students.remove(s)
            count += 1

    print(f"[删除学生] 完毕! 共删除 {count} 条记录!")
    save()  # 删除学生后自动存档


def save():
    """存档函数"""
    with open('D:\Coding\Python', 'w', encoding='utf-8') as f:
        for s in students:
            f.write(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['className']}\n")
    print(f"[存档成功] 共存储了 {len(students)} 条记录!")


def load():
    """读档函数"""
    # 如果存档文件不存在，则跳过读档环节
    if not os.path.exists('D:\Coding\Python'):
        return

    # 先清空全局变量里的数据
    global students
    students = []

    with open('D:\Coding\Python', 'r', encoding='utf-8') as f:
        for line in f:
            # 去除末尾的换行符
            line = line.strip()

            tokens = line.split('\t')

            if len(tokens) < 4:
                print(f"文件格式有误! line={line}")
                continue

            student = {
                "studentId": tokens[0],
                "name": tokens[1],
                "gender": tokens[2],
                "className": tokens[3]
            }

            students.append(student)

    print(f"[读档成功] 共读取了 {len(students)} 条记录!")


if __name__ == "__main__":
    main()