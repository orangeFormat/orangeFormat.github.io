---
title: python数据结构与算法分析_算法分析
date: 2020-01-06 21:48:03
categories: 
- 数据结构
- 算法
- python
tags:
- 笔记
---

## 二、算法分析

1. 什么是算法分析
   - 参数n常被称为问题规模，当n增长时，T(n)增长最快的部分被称为大*O*记法（O指order）。
  
        |f(n)       |名称 |
        | ---        | ---  |
        |  1         | 常数    |
        |  logn      |  对数   |
        |    n       |   线性  |
        |     nlogn  |   对数线性  |
        |     n*n |       平方  |
        |  pow(2,n)  |    指数 |
2. 异序词检测示例
   - 要展示不同数量级的算法，一个好的例子时经典的异序词检测问题。如果一个字符串只是重排了另一个字符串的字符，那么这个字符串就是另一个的异序词，如heart和earth，为了简化问题，假设两个字符串长度相等，并且都是由26个英文字母的小写形式组成的。目标时编写一个布尔函数，接收两个字符串，并能判断它们是否为异序词。
   1. 清点法 

        清点第一个字符串的每个字符，看看他们是否都出现在第二个字符串中。如果是，那么两个字符串必然是异序词。
   2. 排序法

    ``` python
    def anagramSolution(s1, s2):
        alist1 = list(s1)
        alist2 = list(s2)

        alist1.sort()
        alist2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]: 
            pos = pos + 1
        else
            matches = False

        return matches
    ```

    调用两次sort是有代价的，所以这个算法的复杂度不是O(n).

   3. 蛮力法

    穷尽所有的可能，n!增长，比指数增长还要快。

   4. 计数法
    
    两个异序词拥有同样数目的a,b,c等等。要判断两个字符串是否为异序词，先数一下每个字符出现的次数，使用26个计数器，最后，如果两个计数器列表相同，那么两个字符串肯定是异序词。

    ``` python
    def anagramSolution(s1, s2):
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] - 1

        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] = c2[pos] + 1

        j = 0

        stillOK = True
        while j < 26  and stillOK:
            if c1[j] == c2[j]
                j = j + 1
            else:
                stillOK = False
        return stillOK
    ```

    这个方案的循环没有嵌套。这个算法用空间换了时间。很多时候，都需要在时间和空间之间进行权衡
