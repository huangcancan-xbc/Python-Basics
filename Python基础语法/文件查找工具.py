import os
# input_path = input("请输入要查找的文件夹路径：")
# pattern = input("请输入要搜索的关键词：")
#
# for dirpath, dirnames, filenames in os.walk(input_path):
#     print('-------------------------------------------------------------')
#     print(f'文件路径·: {dirpath}')
#     for name in dirnames:
#         print(f'文件名称: {name}')
#     print(f'文件名称: {filenames}')
#     for name in filenames:
#         print(name)

input_path = input("请输入要查找的文件夹路径：")
pattern = input("请输入要搜索的关键词：")

for dirpath, _, filenames in os.walk(input_path):
    for f in filenames:
        if pattern in f:
            print(f'文件路径: {dirpath}')
            print(f'文件名称: {f}')

