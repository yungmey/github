import sys
fuhao = r'''~!@#$%^&*()_+-=[]{};'\:"|,./<>?'''
digit = '0123456789'
alpha = 'qwertyuioplkjhgfdsazxcvbnmMNBVCXZLKJHGFDSAPOIUYTREWQ'

userDB = {'admin': '123', 'hc': '789', 'ym': '789'}
bookDB = [['《西游记》', '古典小说', '吴承恩', 9.99, '热门'],
          ['《三国演义》', '古典小说', '罗贯中', 19.99, '平款'],
          ['《哈利波特》', '魔法小说', 'J.K.罗琳', 19.99, '畅销'],
          ['《王小波文集》', '现代小说', '王小波', 20.99, '畅销'],
          ['《席慕蓉诗选》', '诗歌', '席慕蓉', 0.99, '无人问津']
          ]
print('*****欢迎进入图书管理系统******')
while True:
    r1 = input('1:登陆  2：注册 \n ')
    if r1 == '1':
        flag = 0
        while flag == 0:
            name = input('请输入账号：\n')
            pwd = input('请输入密码：\n')
            if (name, pwd) in userDB.items():
                print('登陆成功，欢迎进入图书系统')
                while 1:
                    print(
                        '1.查看所有书籍\t 2.通过书名查看一本书\n'
                        '3.通过类别查看书籍\t4.通过作者查看书籍\n'
                        '5.通过价格查看一本书\t6.修改一本书\n'
                        '7.删除一本书\t  8.增加一本书\n'
                        '9.退出系统\n')
                    r2 = input('请输入选择：\n')
                    if r2 == '1':
                        print('书名 \t类别 \t作者 \t价格 \t畅销度')
                        for i in bookDB:
                            for j in i:
                                print(j, end='\t')
                            print()

                    elif r2 == '2':
                        while True:
                            bookname = input('请输入要查找的书名：\n')
                            flag1 = 1
                            for i in bookDB:  # 遍历出每本书的信息
                                if bookname == i[0]:  # 判断书名是否在其中的一本

                                    print('书名 \t类别 \t作者 \t价格 \t畅销度')
                                    for j in i:
                                        print(j, end='\t')
                                        flag1 = 0

                            if flag1 == 1:
                                print('书库中没有此书')
                                on = input('请问你要继续查找吗？\n'
                                           ' y/n 输入y继续查找 输入n则返回上一级\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('无法识别你的指令,默认返回上一级')
                                    break
                    elif r2 == '3':
                        while True:
                            style = input('请输入查找书的分类：\n')
                            flag2 = 1
                            for i in bookDB:
                                if style == i[1]:
                                    for j in i:
                                        print('书名 \t类别 \t作者 \t价格 \t畅销度')
                                        print(j, end='\t')
                                        flag2 = 0
                            if flag2 == 1:
                                print('没有此类别的书籍')
                                print('请问是否继续查找：y/n'
                                      '输入y继续查找，n则返回上一步')
                                on = input('输入选择指令：\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('输入指令错误，默认返回上一步')
                                    break

                    elif r2 == '4':
                        while True:
                            art = input('请输入要查找作者：\n')
                            flag4 = 1
                            for i in bookDB:
                                if art == i[2]:
                                    for j in i:
                                        print('书名 \t类别 \t作者 \t价格 \t畅销度')
                                        print(j)
                                        flag4 = 0
                            if flag4 == 1:
                                print('没有此作者的书籍')
                                print('请问是否继续查找：y/n'
                                      '输入y继续查找，n则返回上一步')
                                on = input('输入选择指令：\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('输入指令错误，默认返回上一步')
                                    break




                    elif r2 == '5':
                        while True:
                            price = input('请输入价格查找：\n')
                            flag3 = 1
                            for i in bookDB:
                                price1 = i[3]
                                if price == str(price1):
                                    for j in i:
                                        print('书名 \t类别 \t作者 \t价格 \t畅销度')
                                        print(j, end='\t')
                                        flag3 = 0

                            if flag3 == 1:
                                print('书库中没有此书')
                                on = input('请问你要继续查找吗？\n'
                                           ' y/n 输入y继续查找 输入n则返回上一级\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('无法识别你的指令,默认返回上一级')
                                    break

                    elif r2 == '6':
                        while True:
                            shumin = input('输入要修改的书名：\n')
                            flag5 = 1
                            for i in bookDB:
                                if shumin == i[0]:
                                    print('书名 \t类别 \t作者 \t价格 \t畅销度')
                                    a = []
                                    a.append(input('书名 \t类别 \t作者 \t价格 \t畅销度 \n'))
                                    bookDB[bookDB.index(i)] = a
                                    print('修改成功')
                                    flag5 = 0

                            if flag5 == 1:
                                print('书库中没有此书')
                                on = input('请问你要继续查找吗？\n'
                                           ' y/n 输入y继续查找 输入n则返回上一级\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('无法识别你的指令,默认返回上一级')
                                    break

                    elif r2 == '7':
                        while True:
                            bookname3 = input('输入要删除的书名：\n')
                            flag6 = 1
                            for i in bookDB:
                                if bookname3 == i[0]:
                                    bookDB.remove(i)
                                    print('删除成功')
                                    flag6 = 0

                            if flag6 == 1:
                                print('书库中没有此书')
                                on = input('请问你要继续查找吗？\n'
                                           ' y/n 输入y继续查找 输入n则返回上一级\n')
                                if on == 'y':
                                    continue
                                elif on == 'n':
                                    break
                                else:
                                    print('无法识别你的指令,默认返回上一级')
                                    break
                    elif r2 == '8':
                        while True:
                            b = []
                            b.append(input('书名 \t类别 \t作者 \t价格 \t畅销度 \n'))
                            bookDB.append(b)
                            print('增加书籍成功')
                            c = input('要继续添加书籍吗 y/n '
                                      '输入y继续添加，输入n返回上一步 \n')
                            if c == 'y':
                                continue
                            elif c == 'n':
                                break
                            else:
                                print('无法识别操作，默认返回上一步')
                                break

                    elif r2 == '9':
                        print('欢迎下次光临')
                        sys.exit()
                    else:
                        print('输入错误')

    elif r1 == '2':
        flag10 = 1
        while flag10 == 1:
            name = input('请输入用户名：\n')
            if name in userDB:
                print('用户已存在，请重新输入用户名！')
                continue

            while flag10 == 1:
                pwd = input('请输入密码：\n')
                u = len(pwd)
                num = 0
                for i in pwd:
                    if i in fuhao:
                        num += 1
                        break
                for i in pwd:
                    if i in alpha:
                        num += 1
                        break
                for i in pwd:
                    if i in digit:
                        num += 1
                        break

                if u == 0 or pwd.isspace() == True:
                    print('输入密码不能为空！请重新输入!')

                elif 0 < u <= 8 or pwd.isdigit() == True or pwd.isalpha() == True:
                    print('''您输入的密码安全等级为低！
                           请按以下方式提升您的密码安全级别：
                           1. 密码必须由数字、字母及特殊字符三种组合
                           2. 密码只能由字母开头
                           3. 密码长度不能低于16位
                           请提升你的密码等级
                           ''')
                    continue

                elif u > 16 and pwd[0] in alpha and num == 3:
                    print('您输入的是高级密码！')

                else:
                    print('''您输入的密码安全等级为中级！
                                   请按以下方式提升您的密码安全级别：
                                   1. 密码必须由数字、字母及特殊字符三种组合
                                   2. 密码只能由字母开头
                                   3. 密码长度不能低于16位
                                   请提升你的密码等级
                                   ''')
                    continue
                num1 = input('请确认密码：\n')
                if pwd == num1:
                    userDB[name] = pwd
                    print('注册成功！')
                    flag10 = 0
                else:
                    print('两次密码不一致，请重新输入')
    else:
        print('输入错误,请重新输入')





















       
      
      
      







      
