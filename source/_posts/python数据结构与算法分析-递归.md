---
title: python数据结构与算法分析_递归
date: 2020-01-08 19:36:30
categories: 
- 数据结构
- 算法
- python
tags:
- 笔记
---

### 1、定义

递归是解决问题的一种方法，他将问题不断地分成更小地问题，直到子问题可以用普通地方法解决。通常情况下，递归会使用一个不断调用自己的函数。

```python
# 递归求和函数
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
```

我们需要将一系列调用看作看作一系列简化操作。每一次递归调用都是在解决一个更小的问题，如此下去，直到问题本身不能再简化为止，开始拼接所有子问题的答案，以此解决最初的问题。

### 2、递归三原则

1. 递归算法必须有基本情况
2. 必须改变其状态并向基本情况靠近
3. 必须递归的调用自己

### 3、将整数转换成任意进制的字符串

整个算法包含三个组成部分

- 将原来的整数分成一系列仅有单数伪的数
- 通过查表将单位数转换成字符串
- 连接得到的字符串，从而形成结果

#### 3.1 python实现

```python
def toStr(n, base):
    convertString = "0123456789abcdef"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]
```

#### 3.2 栈帧：实现递归

假设不拼接递归调用toStr的结果和convertString的查找结果，而是再进行递归调用之前把字符串压入栈中。

```python
rStack = Stack()

def toStr(n, base):
    ConvertString = "0123456789abcdef"
    if n < base:
        return rStack.push(ConvertString[n])
    else:
        rStack.push(ConvertString[n % base])
        toStr(n // base, base)
```

### 4、递归可视化

#### 4.1 小乌龟绘图

这个简单函数的基本情况是，要画的线的长度降为零。

```python
from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-4)

drawSpiral(myTurtle, 200)
myWin.exitonclick()
```

#### 4.2 分形树

```python
from turtle import *

t = Turtle()
myWin = t.getscreen()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

tree(110, t)
myWin.exitonclick()
```

#### 4.3 谢尔平斯三角形

```python
from turtle import *

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()
def getMid(p1, p2):
    return ( (p1[0]+p2[0]) /2, (p1[1] + p2[1]) / 2)
def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow','violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],getMid(points[0], points[1]),getMid(points[0], points[2])],degree-1, myTurtle)
        sierpinski([points[1],getMid(points[0], points[1]),getMid(points[1], points[2])],degree-1, myTurtle)
        sierpinski([points[2],getMid(points[2], points[1]),getMid(points[0], points[2])],degree-1, myTurtle)
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-500, -250), (0, 500), (500, -250)]
sierpinski(myPoints, 5, myTurtle)
myWin.exitonclick()
```

### 5、动态规划

在解决优化问题时，一个策略是动态规划。

贪婪算法——试图最大程度的程度的解决问题。

#### 5.1 找零问题的递归解决方案

```python
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMC([1, 5, 10, 25], 63))
```

它的效率非常低，针对找零63分的情况，它需要进行67 716 925次递归调用才能找到最优解。该算法将大量时间和资源浪费在了重复计算已有的结果上。

#### 5.2 添加查询表之后的找零算法

减少计算量的关键是记住已有的记过，简单的做法是把最少硬币数的结果存储在一张表中，并在计算新的最少硬币书之前，检查结果是否已在表中。如果是，就直接使用结果，而不是重新结算。

```python
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

b = recDC([1, 5, 10, 25], 63, [0]*64)
print(b)
```

这个方法所做的优化并不是动态优化，而是通过记忆化（或者叫做缓存）的方法来优化程序的性能。真正的动态规划会用更系统的方法来解决问题

#### 5.3 用动态规划算法解决找零问题

```python
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
            minCoins[cents] = coinCount
        return minCoins[change]
```

```python
# 增加缓存后的动态规划算法
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin  # 妙呀
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

cl = [1, 5, 10, 25]
coinsUsed = [0]*64
coinCount = [0]*64
dpMakeChange(cl, 63, coinCount, coinsUsed)
printCoins(coinsUsed, 63)
```

### 6、小结

- 所有递归算法都必须有基本情况
- 递归算法必须改变其状态并向基本情况靠近
- 必须递归的调用自己
- 在某些情况下可以代替循环
- 往往与问题的形式化表达相对应
- 递归并非总是最佳方案，有时，递归算法比其他算法的计算复杂度更高