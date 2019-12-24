---
title: JS语法
date: 2019-12-24 18:46:10
tags:
- 笔记
- JS
categories:
- W3C
---

### 输出
- 使用 window.alert() 写入警告框
  ```javascript
  <script>
  window.alert(5 + 6);
  </script>
  ```
- 使用 document.write() 写入 HTML 输出
  ```html
  <button onclick="document.write(5 + 6)">试一试</button>
  ```
- 使用 innerHTML 写入 HTML 元素
  ```javascript
  <script>
  document.getElementById("demo").innerHTML=5 + 6;
  </script>
  ```
- 使用 console.log() 写入浏览器控制台
  ```javascript
  <script>
  console.log(5 + 6);
  </script>
  ```

### JavaScript关键字
| 关键字 | 描述 |
| :----- | :---- |
| break | 终止 switch 或循环。 |
| continue | 跳出循环并在顶端开始。 |
| do...while | 停止执行 JavaScript，并调用调试函数（如果可用）。 |
| for | 执行语句块，并在条件为真时重复代码块。 |
| function | 声明函数。 |
| if...else | 标记需被执行的语句块，根据某个条件。 |
| return | 退出函数。 |
| switch | 标记需被执行的语句块，根据不同的情况。 |
| try ... catch | 对语句块实现错误处理。 |
| var | 声明变量。 |

### 语法
  javascript语法是一套规则，它定义了JavaScript地语言结构
  ```javascript
  var x, y;     //如何声明变量
  x = 7; y = 8; //如何赋值
  z = x + y;    //如何计算值
  ```
- 变量
  
  JS使用 **var**关键字来声明变量，**=**号为变量赋值
- 注释
  
  双斜杠 //或 /* 与 */之间地代码被视为注释
- 标识符
  
  标识符首字母必须是字母、下划线或者美元符号
### 函数
  
  &emsp;&emsp;JavaScript 函数通过 function 关键词进行定义，其后是函数名和括号 ()。
  
  &emsp;&emsp;函数名可包含字母、数字、下划线和美元符号（规则与变量名相同）。
  ```javascript
  function myFunction(p1, p2) {
    return p1 * p2;              // 该函数返回 p1 和 p2 的乘积
}
  ```

### 对象

 1. this关键字引用该函数地拥有者，在下面地例子中，this指的是“拥有” fullName 函数的 person 对象。
    ```javascript
    var person = {
        firstName: "Bill",
        lastName : "Gates",
        id       : 678,
        fullName : function() {
    return this.firstName + " " +   this.lastName;
        }
    };
    ```
2. 访问对象属性
    ```javascript
    objectName.propertyName
    ```
    ```javascript
    objectName["propertyName"]
    ```
# 下一节待续   JavaScript事件

### tips
1. 把数值和字符串相加地时候，JS将把数值视作字符串
2. JS从左向右计算表达式
3. JS拥有动态类型，意味着相同变量可用作不同类型
4. JavaScript对大小写敏感
5. 可以使用typeof来确定变量地类型
   ``` javascript
   typeof ""                  // 返回 "string"
   typeof "Bill"              // 返回 "string"
   typeof 0                   // 返回 "number"
   ```
6. 如果通过关键词 "new" 来声明 JavaScript 变量，则该变量会被创建为对象：
   ``` javascript
   var x = new String();        // 把 x 声明为 String 对象
   var y = new Number();        // 把 y 声明为 Number 对象
   var z = new Boolean();       //	把 z 声明为 Boolean 对象
   ```
   请避免字符串、数值或逻辑对象。他们会增加代码的复杂性并降低执行速度。
