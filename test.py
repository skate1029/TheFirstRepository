__author__ = 'skate'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
from functools import reduce
print("###########good begin###########")
print("包含中文的str")
print( '\u4e2d\u6587')
str1 = "中文"
str2 = 'chinese'
bb = str1.encode('utf-8')
print(bb)

print(str1, "的长度为:", len(str1))

l = [1,2,3,]
s = set(l)
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)

#disct&set
dictA = {}
tupleA = (1,2,3)
tupleB = (1,4,6)
dictA[tupleA]='123'
dictA[tupleB]='456'
#setA = set(tupleB)
print("dict&set.")
for k in dictA:
    print(k,dictA[k])
#print("setA=",setA)

#递归函数
def fact(n):
    r, m = 1, 1
    if n == 1:
        r = 1
    while m < n:
        m = m + 1
        r = r * m
    return r

print(fact(10))

def fact1(n):
    r, m = 1, 1
    while m <= n:
        r = r * m
        m = m + 1
    return r

print (fact1(10))

def fact2(n):
    if n == 1:
        return 1
    else:
        return n*fact2(n-1)

print(fact2(3))

def sum1(n):
    if n == 1:
        return 1
    else:
        return n + sum1(n-1)

print(sum1(100))

#汉诺塔
global g_a
g_a = 0
sum2 = [0,]
def move(n, a, b, c):
    if n == 1:
        #global g_a
        #g_a = g_a + 1
        sum2[0] = sum2[0] + 1
        print(a, "-->", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1,b, a, c)
move(3,'A','B','C')
print("总共移动", sum2[0], "次")


#slice
t_List = list(range(10))
print(t_List[:5])
t_List1 = t_List[:]
print(t_List1[:])
print(t_List1[-1::-1])
print(t_List1[::-1])
print(t_List1[4::])

print(t_List1[0:4:1])
print(t_List1[::-1])

#
t_List2 = []
for i in range(11):
    t_List2.append(i*i)

print(t_List2)

t_List3 = [v*v for v in range(11)]
print(t_List3)

t_List4 = [x+y for x in 'ABC' for y in 'XYZ']
print(t_List4)

t_List5 = ['Hello', 'World', 18, 'Apple', None]

t_List6 = [s.lower() for s in t_List5 if isinstance(s,str)]

print(t_List6)

def funcall(x, *fun):
    return [f(x) for f in fun]

print(funcall(10,abs,sqrt))

def funxx(x):
    return x*x
t_List7 = list(range(11))

r = map(funxx,t_List7)
print(list(r))

r = map(str,t_List7)
print(list(r))

def add(x,y):
    return x+y

r = reduce(add,t_List7)

print(r)

def adjust(s):
    return s[0:1].upper() + s[1::].lower()

print(adjust("ASDFv"))
t_List8 = ['adam', 'LISA', 'barT', "LIJIANSS"]
r = map(lambda s:s[0:1].upper() + s[1::].lower(),t_List8)

print(list(r))
t_List9 = list(range(10))
print(t_List9)
print(sum(t_List9))
print(t_List8[0])
#
def prod(L):
    return reduce(lambda x, y : x*y, L)

print(prod([3,5,7,9]))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def fn(x,y):
    return 10*x + y
def str2float(s):
    L = s.split('.')

    r = reduce(fn,map(char2num,L[0])) + reduce(fn,map(char2num,L[1]))/(10**(len(L[1])))
    return r

print(str2float('123.456'))



