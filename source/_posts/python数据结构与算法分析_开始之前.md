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

        BinaryGate类增添的唯一行为就是取得两个输入值，UnaryGate类也有类似的实现，不过它只有一个输入

        ``` python
        # 子类UnaryGate(self):
        class UnaryGate(logicGate):

            def __init__(self, n):
                super().__init__(n)

                self.pin = None

            def getPin(self):
                return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))

        ```

        connect类-并不在逻辑门的继承层次结构中，但是它会使用该结构，从而使每一个连接器的两端都有一个逻辑门，这被称为HAS-A关系。

        ``` python
        # Connector类
        class Connector:
            def __init__(self, fgate, tgate):
                self.fromgate = fromgate
                self.togate = tgate

                tgate.setNextPin(self).

            def getFrom(self):
                return self.fromgate

            def getTo(self):
                return self.togate

        def setNextPin(self, source):
            if self.pinA == None:
                self.pinA = Source
            else:
                if self.pinB == None:
                    self.pinB = source
        ```

### 小结

- 计算机科学使研究如何解决问题的学科
- 计算机科学利用抽象这一工具来表示过程和数据
- 抽象数据类型通过隐藏数据的细节来使程序员能够管理问题的复杂度
- python易用，面向对象编程
- 列表、元组 以及字符串是python的内建有序集合
- 字典和集是无序集合
- 类使程序员能实现抽象数据类型
- 既可以重写标准方法，也可以构建新的方法
- 类可以通过继承层次结构来组织
- 类的构造方法总是调用其父类的构造方法，然后才处理自己的数据和行为
