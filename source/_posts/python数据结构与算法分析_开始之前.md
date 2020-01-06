---
title: python 数据结构与算法分析_开始之前
date: 2020-01-05 15:53:56
categories: 
- 数据结构
- 算法
- python
tags:
- 笔记
---
## 一、导论
1. 计算机科学的研究对象是问题、解决问题的过程，以及通过该过程得到的解决方案。
2. 编程是指通过编程语言将算法编码以使其能被执行的过程。计算机科学的研究对象并不是编程，但是编程是计算机科学家所作工作的一个重要组成部分。
3. python的内建集合数据类型
   1. 列表是零个或多个指向python数据对象的引用的有序集合。列表是异构的，意味着其指向的数据对象不需要都是同一个类，
   2. 元组不可修改
   3. 集合（set)是由零个或多个不可修改的python数据对象组成的无序集合。不允许重复元素，由大括号包含，逗号分隔
   4. 字典是无序结构，由相关的元素对构成，其中每对元素都由一个键和一个值组成。
4. python的异常处理
5. python的类
   1. 定义新的类
        ```python
        class NameOfClass:
            # 方法定义
        ```
   2. 所有类都应该首先提供构造方法。构造方法定义了数据对象的创建方式。python中的构造方法命名为__init__
        ```python
        class NameOfClass:
            
            def __init__(self, top, bottom):

                self.num = top
                self.den = bottom
        ```
        self是一个指向对象本身的特殊参数，必须是第一个形式参数
    3. 继承
       1. 继承使一个类与另一个类相关联，python的子类可以从父类继承特征数据和行为，父类也称为超类。
        ```python
        # 父类LogicGate
        class LogicGate:
            
            def __init__(self, n):
                self.label = n
                self.output = None
            
            def getLabel(self):
                return self.label

            def getOutput(self):
                self.output = self.performaGateLogic()
                return self.output
        ```
        ```python
        # 子类BinaryGate
        class binaryGate(LogicGate):

            def __init__(self, n):
                super().__init__(n)

                self.pinA = None
                self.pinB = None

            def getPinA(self):
                return int(input("Enter Pin A input for Gate " + \
                            self.getLabel() + "-->"))
            def getPinB(self):
                return int(input("Enter Pin B input for Gate " + \
                            self.getLabel() + "-->"))
 
        ```
        
        
        ```python

        # 子类UnaryGate(self):
        class UnaryGate(logicGate):
            
            def __init__(self, n):
                super().__init__(n)

                self.pin = None

            def getPin(self):
                return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
        
        ```
        BinaryGate类增添的唯一行为就是取得两个输入值，UnaryGate类也有类似的实现，不过它只有一个输入

