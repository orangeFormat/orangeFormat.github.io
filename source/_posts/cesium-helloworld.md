---
title: cesium helloworld
date: 2019-12-24 21:18:45
tags:
- 笔记
categories:
- cesium
---
##  一、开始使用
### 1、创建文件夹
```cmd
mkdir cesium_test
cd cesium_test
```
### 2、将cesium源码中的Build文件夹拷入cesium_test
### 3、将cesium源码中Apps文件夹中的HelloWorld.html拷入cesium_test文件夹中
### 4、修改HelloWorld.html中Cesium.js和widgets.css的文件路径
### 5、发布

## 二、界面介绍
![](https://res.cloudinary.com/orangeformat/image/upload/v1577198352/orangeformat/a_iii0j0.jpg)
1. Geocoder: 查找为止工具，查找到之后会将镜头对准找到的地址，默认使用bing地图
2. Home Button: 视角返回初始位置
3. Scene Mode Picker：选择视角的模式，有三种： 3D,2D,哥伦布视图（CV）
4. Base Layer Picker： 图层选择器，选择要显示的地图服务和地形服务。
5. Navigation Help Button: 导航帮助按钮，显示默认的地图控制帮助。
6. Animation： 动画器件，控制视图动话的播放速度。
7. TimeLine：时间线，指示当前时间，并允许用户跳到特定的时间
8. Credits Display: 版权显示，显示数据归属，必选
9. Full screen Button：全屏按钮。