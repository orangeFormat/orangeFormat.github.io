---
title: W3school_TCP/IP笔记“
date: 2019-12-24 17:39:43
tags:
- 笔记
- TCP/IP
categories:
- W3C
---
## 什么是TCP/IP
&emsp;&emsp;TCP/IP是供已连接因特网的计算机进行通信的通信协议。

&emsp;&emsp;TCP/IP指传输控制协议/网际协议(Transmisson Control protocol / Internet Prototcl).

&emsp;&emsp;TCP/IP 定义了电子设备（比如计算机）如何连入因特网，以及数据如何在它们之间传输的标准。

&emsp;&emsp;TCP/IP中包含一系列用于处理数据通信的协议：
1. TCP (传输控制协议) - 应用程序之间通信
   1. 当应用程序希望通过TCP与另一个应用程序通信的时候，它会发送一个通信请求。这个请求必须被送到一个确切的地址。在双方“握手”之后，TCP将在两个应用程序之间建立一个全双工（full_duplex)的通信。
   2. 这个全双工的通信将占用两个计算机之间的通信线路，直到它被一方或双方关闭为止。
   3. UDP和TCP很相似，但是更简单，同时可靠性低于TCP
2. UDP (用户数据包协议) - 应用程序之间的简单通信
3. IP (网际协议) - 计算机之间的通信
   1. IP用于计算机之间的通信
   2. IP是无连接的通信协议。他不会占用两个正在通信的计算机之间的通信线路。这样，IP就降低了对网络线路的需求。每条线可以同时满足许多不同的计算机之间的通信需要。
   3. 通过IP，消息被分割为小的独立的包，并通过因特网在计算机之间传送。
   4. IP负责将两个包路由至它的目的地。
4. ICMP (因特网消息控制协议) - 针对错误和状态
5. DHCP (动态主机配置协议) - 针对动态寻址
6. IP路由器
   1. 当一个IP包从一个计算机被发送，它会到达一个IP路由器。
   2. IP路由器负责将这个包路由至它的目的地，直接的活着通过其他路由器。
   3. 在一个相同的通信中，一个包所经过的路径可能和其他的包不同。而路由器负责根据通信量，网络中的错误或者其他参数来进行正确地寻址。

7. TCP/IP 
   1. TCP/IP意味着TCP和IP在一起协同工作
   2. TCP负责应用软件和网络软件之间地通信
   3. IP负责计算机之间地通信
   4. TCP负责将数据分割并装入IP包，然后再他们到达地时候重新组合它们
   5. IP负责将包发送至接受者

## TCP/IP寻址 
1. IP地址
2. TCP使用固定地连接
   1. TCP 用于应用程序之间的通信。
   2. 当应用程序希望通过 TCP 与另一个应用程序通信时，它会发送一个通信请求。这个请求必须被送到一个确切的地址。在双方“握手”之后，TCP 将在两个应用程序之间建立一个全双工 (full-duplex) 的通信。
   3. 这个全双工的通信将占用两个计算机之间的通信线路，直到它被一方或双方关闭为止
   4. UDP 和 TCP 很相似，但是更简单，同时可靠性低于 TCP。 

## TCP/IP协议

&emsp;&emsp;TCP/IP 是不同的通信协议的大集合。
#### TCP - 传输控制协议
&emsp;&emsp;TCP 用于从应用程序到网络的数据传输控制。

&emsp;&emsp;TCP 负责在数据传送之前将它们分割为 IP 包，然后在它们到达的时候将它们重组。
#### IP - 网际协议
&emsp;&emsp;IP 负责计算机之间的通信。

&emsp;&emsp;IP 负责在因特网上发送和接收数据包。
#### HTTP - 超文本传输协议
&emsp;&emsp;HTTP 负责 web 服务器与 web 浏览器之间的通信。

&emsp;&emsp;HTTP 用于从 web 客户端（浏览器）向 web 服务器发送请求，并从 web 服务器向 web 客户端返回内容（网页）。
#### HTTPS - 安全的 HTTP
&emsp;&emsp;HTTPS 负责在 web 服务器和 web 浏览器之间的安全通信。

&emsp;&emsp;作为有代表性的应用，HTTPS 会用于处理信用卡交易和其他的敏感数据。

#### SSL - 安全套接字层
&emsp;&emsp;SSL 协议用于为安全数据传输加密数据。

#### SMTP - 简易邮件传输协议
&emsp;&emsp;SMTP 用于电子邮件的传输。

#### MIME - 多用途因特网邮件扩展
&emsp;&emsp;MIME 协议使 SMTP 有能力通过 TCP/IP 网络传输多媒体文件，包括声音、视频和二进制数据。

#### IMAP - 因特网消息访问协议
&emsp;&emsp;IMAP 用于存储和取回电子邮件。

#### POP - 邮局协议
&emsp;&emsp;POP 用于从电子邮件服务器向个人电脑下载电子邮件。

#### FTP - 文件传输协议
&emsp;&emsp;FTP 负责计算机之间的文件传输。

#### NTP - 网络时间协议
&emsp;&emsp;NTP 用于在计算机之间同步时间（钟）。

#### DHCP - 动态主机配置协议
&emsp;&emsp;DHCP 用于向网络中的计算机分配动态 IP 地址。

#### SNMP - 简单网络管理协议
&emsp;&emsp;SNMP 用于计算机网络的管理。

#### LDAP - 轻量级的目录访问协议
&emsp;&emsp;LDAP 用于从因特网搜集关于用户和电子邮件地址的信息。
#### ICMP - 因特网消息控制协议
&emsp;&emsp;ICMP 负责网络中的错误处理。
#### ARP - Address Resolution Protocol
&emsp;&emsp;ARP - 用于通过 IP 来查找基于 IP 地址的计算机网卡的硬件地址。

#### RARP - Reverse Address Resolution Protocol
&emsp;&emsp;RARP 用于通过 IP 查找基于硬件地址的计算机网卡的 IP 地址。

#### BOOTP - Boot Protocol
&emsp;&emsp;BOOTP 用于从网络启动计算机。

#### PPTP - 点对点隧道协议
&emsp;&emsp;PPTP 用于私人网络之间的连接（隧道）
