#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


option = '''
--------- 请选择功能 ---------
1. 查询员工工资
2. 修改员工工资
3. 增加新员工记录
4. 退出
---------- The End ----------
'''


def search(argument):
        flag = False
        with open('info.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.split()[0] == argument:
                    flag = True
                    print('\033[31;1m%s\033[0m 的工资是 \033[31;1m%s\033[0m' % (argument, line.split()[1]))
                else:
                    continue

        if not flag:
            print('未找到员工\033[31;1m%s\033[0m信息' % argument)


def revise(salary):
    temp = salary.split(' ')
    flag = False
    with open('info.txt', 'r', encoding='utf-8') as read, open('info', 'w', encoding='utf-8') as write:
        for line in read:
            if line.split()[0] == temp[0]:
                write.write(salary + '\n')
                flag = True
            else:
                write.write(line)

    os.rename('info.txt', 'info_bak.txt')
    os.remove('info_bak.txt')
    os.rename('info', 'info.txt')

    if flag:
        print('员工\033[31;1m%s\033[0m 的工资已修改为 \033[31;1m%s\033[0m' % (temp[0], temp[1]))
    else:
        print('未找到员工\033[31;1m%s\033[0m信息' % temp[0])


def add(employment):
    temp1 = employment.split(' ')
    with open('info.txt', 'a+', encoding='utf-8') as f:
        for line in f:
            if line.split(' ')[0] == temp1[0]:
                print('用户\033[31;1m%s\033[0m已存在' % temp1[0])
        else:
            f.write('\n' + employment)
            print('员工信息\033[31;1m%s\033[0m已添加.' % employment)


def cvt2dict(cvt):
    temp2 = cvt.split(' ')
    result = {temp2[0]: temp2[1]}
    return result


stop_flag = False
with open('info.txt', 'r+', encoding='utf-8') as info:
    data = cvt2dict(info.readline())
    print(option)

choice = input('您要选择?')
while not stop_flag:
    if not choice.isdigit():
        choice = input('请输入数字选项编号: ')
    elif int(choice) > 4 or int(choice) < 1:
        choice = input('请输入有效的数字选项编号: ')
    elif int(choice) == 1:
        name = input('请输入要查询员工姓名: ')
        search(name)
        stop_flag = True
    elif int(choice) == 2:
        source = input('请输入要修改员工姓名和工资, 用空格分隔(例如:Alex 10): ')
        revise(source)
        stop_flag = True
        continue
    elif int(choice) == 3:
        source = input('请输入要添加的员工姓名和工资, 用空格分隔(例如:Alex 10): ')
        add(source)
        stop_flag = True
    else:
        stop_flag = True
        print('再见')
