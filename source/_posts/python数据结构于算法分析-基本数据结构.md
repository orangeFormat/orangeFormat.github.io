---
title: python数据结构于算法分析_基本数据结构
date: 2020-01-07 19:43:45
categories: 
- 数据结构
- 算法
- python
tags:
- 笔记
---
### 1、什么是线性数据结构

&emsp;&emsp;某个元素添加进来，它于前后元素的相对位置将保持不变，这样的数据集合被称为线性数据结构。如栈、队列、双端队列、列表。

### 2、栈
&emsp;&emsp;添加操作和移除操作总是发生在同一端，这种排序原则被称为LIFO(last in first out)。

#### 2.1 栈抽象数据类型

&emsp;&emsp;栈抽象数据类型由下面的结构和操作定义。栈是元素的有序集合，添加操作和移除操作都发生在顶端。栈的操作顺序是LIFO，它支持一下操作。

- stack()创建一个空栈。不需要参数，返回一个空栈
- push(item)将一个元素添加到栈的顶端。它需要一个参数item，无返回值
- pop()将栈顶端的元素移除。它不需要参数，但会返回顶端的元素，并且修改栈的内容。
- peek()检查栈顶端的元素，但是并不移除该元素。不需要参数，也不会修改栈的内容
- isEmpty()检查栈是否为空。不需要参数，返回一个布尔值
- size()返回栈中元素的数目。不需要参数，返回一个整数
  
#### 2.2 python实现

```python
class stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
```

&emsp;&emsp;也可以选择将列表的头部作为栈的顶端。不过在这种情况下，便无法直接用pop方法和append方法，而必须用pop方法和insert方法显示的访问下标为零的元素。

&emsp;&emsp;改变抽象数据类型的实习那却保留其逻辑特征，这种能力体现了抽象思想，不过，尽管两种方法都可以实现，但是二者在性能方面肯定由所差异，append方法和pop()方法的时间复杂度都是O(1),但是insert(0)和pop(0)的时间复杂度都是O(n)

### 3、队列

&emsp;&emsp;队列是有序集合，添加操作发生在尾部，移除操作发生在头部，这种操作方式被称为FIFO(first in first out),先进先出

#### 3.1 队列抽象数据类型

- Queue() 创建一个空队列。不需要参数，且返回一个队列。
- enqueue(item) 在队列的尾部添加一个参数。需要一个元素作为参数，不返回任何值
- dequeue() 从队列的头部移除一个元素。 它不需要参数，且会返回一个元素，并修改队列的内容
- isEmpty() 检查队列是否为空，不需要参数，且会返回一个布尔值
- size() 返回队列中元素的数目，不需要修改参数，且会返回一个整数

#### 3.2 python实现

```python
class Queue():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
```

### 4、双端队列

&emsp;&emsp;双端队列是与队列类似的有序集合。它有一前一后两端，元素在其中保持自己的位置。与队列不同的是，双端队列对在那一端添加和移除元素没有任何限制。

#### 4.1 双端队列抽象数据类型

&emsp;&emsp;双端队列是元素的有序集合，其任何一端都允许添加或移除元素。

- Deque() 创建一个空的双端队列。不需要参数，返回一个空的双端队列。
- addFront(item) 将一个元素添加到双端队列的前端。接受一个元素作为参数，没有返回值
- addRear(item) 将一个元素添加到双端队列的后端。它接受一个元素作为参数，没有返回值
- removeFront() 从双端队列的前端移除一个元素。不需要参数，且会返回一个元素，并修改双端队列的内容。
- removeRear() 从双端队列的后端移除一个元素。不需要参数，返回一个元素并修改双端队列的内容
- isEmpty() 检查双端队列是否为空。不需要参数，且会返回一个布尔值
- size() 返回双端队列中元素的数目。u需要参数且会返回一个整数
  
#### 4.2 python实现

```python
class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(slef):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
```

在前端进行的添加操作和移除操作的时间复杂度是O(1),后端的添加和移除操作的时间复杂度是O(n)。

### 5、列表

&emsp;&emsp;之前用了python列表来实现其他抽象数据类型。但是，并非多有的编程语言都有列表。对于不提供列表的编程语言，必须自己动手实现。

&emsp;&emsp;列表是元素的集合，集中每一个元素都有一个相对于其他元素的位置。更具体地说，这种列表称为无序列表。

#### 5.1 无序列表的抽象数据类型

无序列表是元素的集合，其中每一个元素都有一个相对于其他元素的位置。

- List() 创建一个空列表，它不需要参数，且会返回一个空列表
- add(item) 假设元素item之前不在列表中，并向其中添加item。它接受一个元素作为参数，无返回值
- remove(item) 假设元素item已在列表中，并从中移除item，返回一个元素作为参数，并且修改列表
- serach(item)  在列表中搜索元素item。接受一个元素作为参数，返回布尔值
- isEmpty() 检查列表是否为空，不需要参数，并且返回布尔值
- length() 返回列表中元素的个数，不需要参数，并且返回布尔值
- append(item) 假设之前item不在列表中，并在列表最后的位置添加item，它接受一个元素作为参数，无返回值
- index(item) 假设元素item已在列表中，并返回该元素在列表中的位置，它接受一个元素作为参数，并且返回该元素的下标
- isnert(pos, item) 假设元素item之前不在列表中，同时假设pos是合理的值，并在位置pos出添加元素item，他接受俩个参数，无返回值
- pop() 假设列表不为空，并移除列表中的最后一个元素，它不需要参数，且会返回一个元素
- pop(pos) 假设在指定位置pos存在元素，并移除该位置上的元素，它节后苏位置参数，且返回一个元素

#### 5.2 实现无序列表：链表

为了实现无序列表，我们要构建链表。无序列表要维持元素之间的相对位置，但是并不需要在连续的内存空间中维护这些位置信息。必须指明列表中第一个元素的位置，然后根据第一个元素的位置，根据其中额链表访问第二个元素，以此类推。

##### 5.2.1 Node类

节点(node)是构建链表的基本数据结构。每一个节点对象都必须持有至少两份信息。首先节点必须包含列表元素，称之为节点的数据变量。其次，节点必须保存指向下一个节点的引用。

python实现

```python
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
```

##### 5.2.2 无序列表的python实现

``` python
class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        pass

    def insert(self, item):
        pass

    def index(self, item):
        pass

    def pop(self, item):
        pass

```

#### 5.3 有序列表的抽象数据类型

在有序列表中，元素的相对位置取决于他们的基本特征。


- OrderedList() 创建一个空有序列表，它不需要参数，且会返回一个空列表
- add(item) 假设元素item之前不在列表中，并向其中添加item。它接受一个元素作为参数，无返回值
- remove(item) 假设元素item已在列表中，并从中移除item，返回一个元素作为参数，并且修改列表
- serach(item)  在列表中搜索元素item。接受一个元素作为参数，返回布尔值
- isEmpty() 检查列表是否为空，不需要参数，并且返回布尔值
- length() 返回列表中元素的个数，不需要参数，并且返回布尔值
- index(item) 假设元素item已在列表中，并返回该元素在列表中的位置，它接受一个元素作为参数，并且返回该元素的下标
- pop() 假设列表不为空，并移除列表中的最后一个元素，它不需要参数，且会返回一个元素
- pop(pos) 假设在指定位置pos存在元素，并移除该位置上的元素，它节后苏位置参数，且返回一个元素
  
#### 5.4 实现有序列表

```python
class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        retrun found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous = None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # 待续。。。。
```

### 6、小结

- 线性数据结构以有序的方式维护其数据
- 栈是最简单的数据结构，其排序原则是LIFO，即后进先出
- 栈的基本操作是push, pop和isEmpty。
- 表达式有三种写法：前序、中序和后序。
- 栈在计算和转换表达式的算法中十分有用。
- 栈具有反转特性
- 双端队列是栈和队列的结合
- 列表是原色的集合，其中每一个元素都有一个相对于其他元素的位置
- 链表保证逻辑顺序，碎石机存储顺序没有要求
- 修改链表头部是一种特殊情况
