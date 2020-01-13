---
title: nodejs环境准备
date: 2020-01-12 14:40:14

categories: 
- nodejs
tags:
- 笔记
---
### 1、nodejs安装


### 2、项目初始化

创建一个目录存放代码，然后初始化项目

```cmd
// 创建 package.json 文件。该文件用于管理项目中用到一些安装包
npm init
```

### 3、koa相关组件安装

#### 安装koa

通过npm命令直接安装

```cmd
// 安装 koa，并将版本信息保存在 package.json 中
npm i koa -S
```

S 或者 --save 是为了安装完成之后能够在 package.json 的 dependencies 中保留 koa-router，以便于下次只需要执行 npm i 或者 npm install 就能够安装所有需要的依赖包。

#### 安装koa-router

通过npm命令直接安装

```cmd
npm i koa-router -S
```

#### 安装koa-bodyparser

通过npm命令直接安装

```cmd
npm i koa-bodyparser -S
```

#### 安装koa-nunjucks-2

通过npm命令直接安装

```cmd
npm i koa-nunjucks-2 -S
```

#### 安装 koa-static 静态资源目录

通过npm命令直接安装

```cmd
npm i koa-static -S
```
