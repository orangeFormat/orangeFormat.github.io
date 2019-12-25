---
title: nodejs笔记
date: 2019-12-25 13:09:48
tags:
- 笔记
categories:
- cesium
---
## 一、一个简单的node.js应用
&emsp;&emsp;Node.js 应用是由以下几部分组成：的：

1. 引入 required 模块：可以使用 require 指令来载入 Node.js 模块。

2. 创建服务器：服务器可以监听客户端的请求，类似于 Apache 、Nginx 等 HTTP 服务器。

3. 接收请求与响应请求 服务器很容易创建，客户端可以使用浏览器或终端发送 HTTP 请求，服务器接收请求后返回响应数据。
   ```javascript
   var http = require('http');

   http.createServer(function (request, response) {

    // 发送 HTTP 头部 
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
      response.writeHead(200, {'Content-Type': 'text/plain'});

      // 发送响应数据 "Hello World"
      response.end('Hello World\n');
     }).listen(8888);

    // 终端打印如下信息
    console.log('Server running at http:// 127.0.0.1:8888/');
    ```

## 二、node.js REPL（交互式解释器）
&emsp;&emsp;node自带了交互式解释器，可以执行以下任务：

- 读取 - 读取用户输入，解析输入了Javascript 数据结构并存储在内存中。

- 执行 - 执行输入的数据结构

- 打印 - 输出结果

- 循环 - 循环操作以上步骤直到用户两次按下 ctrl-c 按钮退出。

Node 的交互式解释器可以很好的调试 Javascript 代码。

## 三、node.js回调函数
&emsp;&emsp;Node.js 异步编程的直接体现就是回调。

&emsp;&emsp;异步编程依托于回调来实现，但不能说使用了回调后程序就异步化了。回调函数在完成任务后就会被调用，Node 使用了大量的回调函数，Node 所有 API 都支持回调函数。 例如，我们可以一边读取文件，一边执行其他命令，在文件读取完成后，我们将文件内容作为回调函数的参数返回。这样在执行代码时就没有阻塞或等待文件 I/O 操作。这就大大提高了 Node.js 的性能，可以处理大量的并发请求。  回调函数一般作为函数的最后一个参数出现：
```javascript
function foo1(name, age, callback) { }
function foo2(value, callback1, callback2) {}
```
#### 阻塞代码
创建一个文本文件input.txt,内容如下
```txt
这是一条测试信息
```
创建main.js文件，代码如下：
```javascript
var fs = require("fs");
var data = fs.readFileSync('input.txt');
console.log(data.toString());
console.log("程序执行结束！")
```

程序运行结果如下：
```cmd
E:\cesium_project\learnNode>node test.js
这是一条测试信息
程序执行结束！
```
#### 非阻塞实例
main.js文件代码如下：
```javascript
var fs = require("fs");
var data = fs.readFileSync('input.txt',function(err,data){
    if(err) return console.error(err);
    console.log(data.toString());
});
console.log("程序执行结束！")
```
程序运行结果如下：
```cmd
E:\cesium_project\learnNode>node test.js
程序执行结束！
这是一条测试信息
```
第一个实例在文件读取完后才执行程序。 第二个实例我们不需要等待文件读取完，这样就可以在读取文件时同时执行接下来的代码，大大提高了程序的性能。

因此，阻塞是按顺序执行的，而非阻塞是不需要按顺序的，所以如果需要处理回调函数的参数，我们就需要写在回调函数内。

## 四、node.js事件循环
&emsp;&emsp;Node.js 使用事件驱动模型，当web server接收到请求，就把它关闭然后进行处理，然后去服务下一个web请求。当这个请求完成，它被放回处理队列，当到达队列开头，这个结果被返回给用户。

&emsp;&emsp;这个模型非常高效可扩展性非常强，因为 webserver 一直接受请求而不等待任何读写操作。（这也称之为非阻塞式IO或者事件驱动IO）在事件驱动模型中，会生成一个主循环来监听事件，当检测到事件时触发回调函数。
#### 实例
创建main.js文件，代码如下所示：
```javascript
// 引入 events 模块
var events = require('events');
// 创建 eventEmitter 对象
var eventEmitter = new events.EventEmitter();
 
// 创建事件处理程序
var connectHandler = function connected() {
   console.log('连接成功。');
  
   // 触发 data_received 事件 
   eventEmitter.emit('data_received');
}
 
// 绑定 connection 事件处理程序
eventEmitter.on('connection', connectHandler);
 
// 使用匿名函数绑定 data_received 事件
eventEmitter.on('data_received', function(){
   console.log('数据接收成功。');
});
 
// 触发 connection 事件 
eventEmitter.emit('connection');
 
console.log("程序执行完毕。");
```
## 五、node.js EventEmitter
Node.js 所有的异步 I/O 操作在完成时都会发送一个事件到事件队列。

Node.js 里面的许多对象都会分发事件：一个 net.Server 对象会在每次有新连接时触发一个事件， 一个 fs.readStream 对象会在文件被打开的时候触发一个事件。 所有这些产生事件的对象都是 events.EventEmitter 的实例。
### EventEmitter类
events 模块只提供了一个对象： events.EventEmitter。EventEmitter 的核心就是事件触发与事件监听器功能的封装。

可以通过require("events");来访问该模块。
# 待续。。。。