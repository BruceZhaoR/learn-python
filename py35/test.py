# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:05:22 2016

@author: xyf
"""

from random import randint, sample
from sys import exit
import time

# 基本信息
u_name = input("输入你的名字: ")
u_id = input("输入你的id: ")

# 选择难度
diff = "s"
while not diff.isdigit():
    print('''难度说明:
    1. 10以内四则运算
    2. 20以内四则运算
    3. 100以内四则运算''')
    diff = input("请选择难度: 1/2/3: ")
    
    
con = "y"
count = 1
m_list = sample(list(range(1,6)) * 2, 10)


# 打开文件
t = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
f = open("%s-%s-%s.txt" % (u_id, u_name, t), "w")

while True:
    
    diff = int(diff)

    if diff == 1:
        n_max = 10
    elif diff == 2:
        n_max = 20
    else:
        n_max = 100    
    
    # 定义随机数-初始值    
    a = randint(1, n_max)
    b = randint(1, n_max)

    # 定义随机数-模式
        
    mode = m_list[count % 10-1]

    # 定义模式选择
    if mode == 1:
        ans_sys = a + b
        desc = "%d + %d"
    elif mode == 2:
        ans_sys = a - b
        desc = "%d - %d"
    elif mode == 3:
        ans_sys = a * b
        desc = "%d * %d"
    elif mode == 4:
        ans_sys = a // b
        desc = "%d // %d"
    elif mode == 5:
        ans_sys = a % b
        desc = "%d %% %d"
            
    
    # 对话框
    print("题目%d是: " % count)
    print(desc % (a, b))
    t_item1 = time.time()
    ans_user = input("请输入答案: ")
       
    
    # 判断句
    if int(ans_user) == ans_sys:
        print("恭喜你！答对了！")      
    else:
        print("很遗憾，你答错了")
        print("正确答案是%d" % ans_sys)
    
    t_item2 = time.time()
    # 用时
    t_item = t_item2 - t_item1
    # 写出
    f.write("%d\t%s\t%d\t%f\t" % (count, ans_user, ans_sys, t_item) + 
            desc % (a, b) + "= %d" % ans_sys + "\t%d" % diff + "\n")
    
    # 是否继续
    if count % 10 == 0:
        print("再爽一波？")
        con = input("Y/N: ")
        if con.lower() != "n":
            print('''about difficulty:
                1. 10以内四则运算
                2. 20以内四则运算
                3. 100以内四则运算    
                ''')
            diff = input("请选择难度: 1/2/3: ")
            while not diff.isdigit():
                print('''about difficulty:
                1. 10以内四则运算
                2. 20以内四则运算
                3. 100以内四则运算    
                ''')
                diff = input("请选择难度: 1/2/3: ")
            m_list = sample(list(range(1,6)) * 2, 10)
    
    count += 1
    
    # 退出  
    if con.lower() == "n":
        print("再见！")
        f.close()
        exit()
    
