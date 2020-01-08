---
title: python数据结构与算法分析_搜索与排序
date: 2020-01-08 22:11:36
categories: 
- 数据结构
- 算法
- python
tags:
- 笔记
---

### 1、搜索

搜索时指从元素集合中找到某个特定元素的算法过程。

#### 1.1 顺序搜索

存储于列表等集合中的数据项彼此存在线性或顺序的关系，每个数据项的位置与其他数据项相关。

无序列表中的时间复杂度是O(n)

在有序列表中，只有当列表中不存在目标元素时，有序排列元素才会提高顺序搜索的效率。

#### 1.2 二分搜索

有序列表中可以利用二分搜索提高搜索效率

```python
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) / 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
```

这个算法时分治策略的好例子。分治是指将问题分解成小问题，以某种方式解决小问题，然后整合结果，已解决最初的问题。

```python
# 二分搜索的递归版本
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midPoint = len(alist) // 2  # 整除
        if alist[midPoint] == item:
            return True
        else:
            if item < alist[midPoint]:
                return binarySearch(alist[:midPoint], item)
            else:
                return binarySearch(alist[midPoint+1:], item)
```

二分算法的时间复杂度是O(logn)

#### 1.3 散列

1. 散列表是元素集合，其中的元素以一种便于查找的方式存储。算列表的每个位置通常被称为槽，其中可以存储一个元素。槽用一个从零开始的整数标记。初始情况下，散列表中没有元素，每个槽都是空的。

2. 散列函数是将散列表中的每个元素与其所属位置对应起来。对散列表中的任一元素，散列函数返回一个介于0和m-1之间的整数。

3. 给定一个元素集合，能够将每个元素映射到不同的槽，这种散列函数称作完美散列函数。如果元素已知，那么构建完美散列函数是可能的，但没有系统化方法来保证散列函数是完美的。

4. 我们的目标是创建这样一个散列函数：冲突数最少，计算方便，元素均匀分布于散列表中。有多种方法扩展取余函数，以下介绍几种。

   - 折叠法 先将元素切成等长的部分，然后将这些部分相加,得到散列值。
   - 平方取中法

5. 处理冲突&emsp;找一个空的槽放着