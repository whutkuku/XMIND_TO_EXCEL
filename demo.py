# -*- coding: utf-8 -*-
'''
  @Time : 2022/6/21 4:45 下午
  @Author : frankkfu
  file: demo.py
  @desc:
'''
import base64
import hashlib
import hmac
import time
import requests

# def test(n):
#     if n==0 :
#         return 1
#     else:
#         return n * test(n-1)
#
#
# while 1:
#     try:
#         a = raw_input("输入一个正整数：")
#         if a == 'quit':
#             break
#         else:
#             print test(int(a))
#             break
#     except:
#         print ("请重新输入正确值")
#######字符串反转，递归函数#########
# def rev(n):
#     if len(n)==1:
#         return n
#     else:
#         return n[-1] + rev(n[0:len(n)-1])
#
# n = raw_input("输入字符串n:")
# print rev(n)
# import random
# # l=[random.randint(-10,10) for _ in range(0,10)]
# # print l
# d = []
# for _ in range(0,10):
#     l = random.randint(-10,10)
#     d.append(l)
# print d
# print min(d)

# a = (i for i in range(0,10))
# print tuple(a)

# import re
# a = "123.4567.890.123"
# b = re.findall(r'(?=(\d+\.\d+))',a)
# print b
# a = 10  #1010
# b = 3   #0011
# a = a ^ b  #0101
# b = a ^ b  #1001
# a = a ^ b  #0011
# print a, b
#
# a = 10
# b = 3
# a, b = b, a
# print a, b

# def del_repeat_char(list):
#     a = []
#     b = []
#     for i in list:
#         if i not in b:
#             a.append(i)
#             b.append(i)
#     return a
#
# list = ['a','b','a','c', 'd', 'c', 'a']
# no_repeat_list = del_repeat_char(list)
# print no_repeat_list

# a, b, c, d = 1, 1, 1000, 1000
# print id(a),id(b),id(c),id(d)
# print(a is b, c is d)
#
# def foo():
#     e = 1000
#     f = 1000
#     print id(e), id(f)
#     print(e is f, e is d)
#     g = 1
#     print id(g)
#     print(g is a)
#
# foo()

# fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x + 1), 1)
# print fac(3)
# b = lambda x: "Even" if x%2==0 else "Odd"
# print b(4)
# print(type([x for x in 'hello world' if x not in 'abcdefg']))
# print(len({x for x in 'hello world' if x not in 'abcdefg'}))
# print type(({x for x in 'hello world' if x not in 'abcdefg'}))

# message = 'hello, world!'
# print(message.replace('o', 'O').replace('l', 'L').replace('he', 'HE'))
# import re
# message = 'helloi, world!'
# pattern = re.compile('[aeiou]')
# print(pattern.sub('#', message))

# def extend_list(val, items=[]):
#     items.append(val)
#     return items
#
# list1 = extend_list(10)
# list2 = extend_list(123, [])
# list3 = extend_list('a')
# print(list1)
# print(list2)
# print(list3)

# class A:
#     def __init__(self, value):
#         self.__value = value
#
#     @property
#     def value(self):
#         return self.__value
#
# obj = A(1)
# obj.__value = 2
# print(obj.value)
# print(obj.__value)

# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# print sorted(prices, key=lambda x: prices[x], reverse=True)


# from collections import namedtuple
#
# Card = namedtuple('Card', ('suite', 'face'))
# card1 = Card('红桃', 13)
# card2 = Card('草花', 5)
# print('{%s},{%s}' % (card1.suite,card1.face))
# # print(f'{card1.suite}{card1.face}')
# # print(f'{card2.suite}{card2.face}')
# class MyCard(Card):
#
#     def show(self):
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return "%s%s" % ({self.suite},{faces[self.face]})
#
#
# print(Card)  # <class '__main__.Card'>
# card3 = MyCard('方块', 12)
# print(card3.show())  # 方块Q
# print(dict(card1._asdict()))  # {'suite': '红桃', 'face': 13}
# print(card2._replace(suite='方块'))

# def duck(n):    #经过第n个村子后剩余的鸭子数
#     if n == 7:
#         return 2
#     else:
#         return (duck(n+1)+1)*2
# for i in range(0,8):
#     if i==0:
#         print ("鸭子总数：%d" %duck(i))
#     else:
#         print ("第%d个村子卖掉的鸭子数为%d，剩余鸭子数为%d" %(i, duck(i-1)-duck(i), duck(i)))

# def jiaogu(step, n):   #角谷定理，任意数为奇数时，乘以3加1，为偶数时除以2，直至最后为1
#     if n==1:
#         return step
#     else:
#         if n%2==0:
#             step +=1
#             print(n / 2),
#             return jiaogu(step, n / 2)
#
#         else:
#             step += 1
#             print(3 * n + 1),
#             return jiaogu(step, 3 * n + 1)
# step = 0
# n = eval(raw_input("n:"))
# s = jiaogu(step, n)
# print ("\n经过%d次运算得到1" % s)
# def apple_num(n,before_num,after_num,m):
#     if n >6:
#         return 0
#     else:
#         print ("第%s个儿子原来有%s个苹果" % (str(n), str(before_num)))
#         give_num = after_num/m
#         next_before_num = 420*(m-1)/(m-2)-give_num
#         next_after_num = give_num + next_before_num
#         n +=1
#         m -=1
#         return apple_num(n, next_before_num, next_after_num, m)
# apple_num(1, 240, 240, 8)

# def num(num):  #闭包
#     def numin(numin):
#         return num + numin
#     return numin
#
# a=num(100)
# b=a(100)
# print b

# def foo(num):
#     print 'starting.........'
#     while num < 1000:
#         num +=1
#         yield num
# for i in foo(0):
#     print i
#     print id(i)
# import re
# #
# #
# # def main():
# #     # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
# #     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
# #     sentence = '''
# #     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
# #     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
# #     '''
# #     # 查找所有匹配并保存到一个列表中
# #     mylist = re.findall(pattern, sentence)
# #     print(mylist)
# #     print('--------华丽的分隔线--------')
# #     # 通过迭代器取出匹配对象并获得匹配的内容
# #     for temp in pattern.finditer(sentence):
# #         print(temp.group())
# #     print('--------华丽的分隔线--------')
# #     # 通过search函数指定搜索位置找出所有匹配
# #     m = pattern.search(sentence)
# #     while m:
# #         print(m.group())
# #         m = pattern.search(sentence, m.end())
# #
# #
# # if __name__ == '__main__':
# #     main()
# -*- coding: utf-8 -*-

from xmindparser import xmind_to_dict
import xlwt

# 记录列数，全局变量，还原方便
columnIndex = 0
# 记录行数
rowIndex = 1
# 每个完整用例子主题的个数
caseCount = 0
# 同层级主题个数
level_equal = 0


if __name__ == '__main__':
    # 用例地址
    file_path = '规则引擎通过变量获取 EO OC 节点国家代码信息.xmind'

    # 使用xlwt模块
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('case', cell_overwrite_ok=True)



    #title_list = ['用例目录', '用例名称', '前提条件', '操作步骤', '期望结果']
    # title_list = ['用例目录', '用例名称', '描述', '等级', '用例类型', '前置条件', '步骤', '预期结果', '是否自动化','标签',
    #               '提测打回次数','预计结束时间','tapd','CI用例','用例编号',	'用例整改','适用平台',	'自动化脚本',	'自动化脚本负责人','迭代']
    title_list = ['用例目录', '用例名称', '描述', '等级', '用例类型', '前置条件', '步骤描述类型', '步骤', '预期结果', '是否自动化', '标签', '关联tapd需求',
                  '提测打回次数', '预计结束时间', 'tapd', 'CI用例', '用例编号', '用例整改', '适用平台', '自动化脚本', '自动化脚本负责人', '迭代']
    # 用例标题写入excel首行
    for j in range(0, len(title_list)):
        ws.write(0, j, title_list[j])
        j += 1

    # 首层画布
    xmind_origin = xmind_to_dict(file_path)
    #print(xmind_origin)

    # 画布跟节点title
    case_title = xmind_origin[0]['topic']['title']
    print(case_title)

    # 主用例
    case_topics = xmind_origin[0]['topic']['topics']

    for i in range(0, len(case_topics)):      # 获取第一层title
        case_title_1 = case_topics[i]['title']
        case_topic_1 = case_topics[i]['topics']

        i += 1
        for j in range(0, len(case_topic_1)):   # 获取第二层title
            case_title_2 = case_topic_1[j]['title']
            case_topic_2 = case_topic_1[j]['topics']
            j += 1

            for x in range(0, len(case_topic_2)):     # 获取第三层title（用例标题）
                case_title_3 = case_topic_2[x]['title']
                case_topic_3 = case_topic_2[x]['topics']
                case_level_3 = case_topic_2[x]['labels'][0]
                x += 1
                caseCount += 1  #记录用例个数
                columnIndex = 1  # 设置用例标题列

                # 写用例目录
                case_dir = case_title + '/' + case_title_1 + '/' + case_title_2
                print('case_dir', case_dir)
                ws.write(rowIndex, 0, case_dir)

                # 写用例标题
                ws.write(rowIndex, columnIndex, case_title_3)

                # 写用例等级
                ws.write(rowIndex, columnIndex + 2, case_level_3)

                # 写用例类型，目前都写 功能测试
                ws.write(rowIndex, columnIndex + 3, '功能测试')
                print('---------------------------------')

                for y in range(0, len(case_topic_3)):
                    case_title_4 = case_topic_3[y]['title']  # 获取第四层title
                    try:
                        case_topic_4 = case_topic_3[y]['topics']
                        print('4', case_title_4, case_topic_4)
                    except Exception as e:
                        print('前提条件为空')
                        case_topic_4 = []
                    y += 1

                    # 写前提条件
                    if case_title_4.encode('utf-8') == '前提条件':
                        qianti_topics_j = []
                        for title in case_topic_4:
                            qianti_topics = title['title'].encode('utf-8')  # unicode编码转str
                            qianti_topics_j.append(qianti_topics)  # 追加内容
                           # qianti = "\n".join([str(e) for e in qianti_topics_j])  # 拼接并换行
                            qianti = "\n".join(
                                [str(i+1) + '.' + qianti_topics_j[i] for i in range(0, len(qianti_topics_j))])
                            ws.write(rowIndex, columnIndex + 1 + 3, qianti)

                    # 写步骤
                    if case_title_4.encode('utf-8') == '步骤':
                        step_topics_j = []
                        for title in case_topic_4:
                            step_topics = title['title'].encode('utf-8')
                            step_topics_j.append(step_topics)
                            #step = "\n".join([str(e) for e in step_topics_j])  # 拼接多个步骤并换行
                            step = "\n".join(
                                [str(i + 1) + '.' + step_topics_j[i] for i in range(0, len(step_topics_j))])
                            ws.write(rowIndex, columnIndex + 2 + 3 + 1, step)

                    # 写预期结果
                    if case_title_4.encode('utf-8') == '期待结果':
                        yuqi_topics_j = []
                        for title in case_topic_4:
                            yuqi_topics = title['title'].encode('utf-8')
                            yuqi_topics_j.append(yuqi_topics)
                            #yuqi = "\n".join([str(e) for e in yuqi_topics_j])
                            yuqi = "\n".join(
                                [str(i + 1) + '.' + yuqi_topics_j[i] for i in range(0, len(yuqi_topics_j))])
                            ws.write(rowIndex, columnIndex + 3 + 3 + 1, yuqi)

                rowIndex += 1

    print('用例总数%s:' % caseCount)

    # 保存Excel文档
    wb.save('export.xls')


