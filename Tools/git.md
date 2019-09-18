## Website Address
[Git](https://git-scm.com/)

## Git for GitHub
[Git Cheat Sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

## 参考
[廖雪峰官方网站git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

## git
Git是一个免费开源的分布式版本控制系统，旨在以速度和效率处理从小型到大型的所有项目。

Git易于学习，占地面积小，性能极快。它超越了诸如Subversion、CVS、Performance和ClearCase这样的配置管理工具，具有廉价的本地分支、方便的临时区域和多个工作流等特性。

[学习文档](https://git-scm.com/docs)

## giteveryday for individual developer
1. git init 创建一个新仓库或者重新初始化一个已有的仓库。
这个命令创建一个空仓库，一个具有objects，ref/heads，refs/tags和模板文件子目录的.git目录。还创建了引用主分支 `HEAD` 的初始 `HEAD` 文件。
2. git log 仓库的操作记录
3. git checkout 和 git branch 切换branches，恢复工作树文件 git branch: master/git checkout: 
4. git add 管理索引文件，更新工作树的当前内容
5. git diff 和 git status查看更新哪些内容
6. git commit 提前当前分支，提交？
7. git reset 和 git checkout（带路径参数）来撤销改变
8. git merge 合并局部分支
9. git rebase
10. git tag

## 常用命令
1、更新工作树
```
git add *
```
2、提交当前修改
```
git commit -m "message"
```
3、推送到远程服务器
```
git push origin master
```
4、从远程服务器下拉
```
git pull
```
[参考](https://git-scm.com/docs/giteveryday)
## Error and Solution
**Error 1** 

从远程库git clone的时候出现Permission Denied

Solution: 原因本机公钥（publickey）未添加至github，所以无法识别。 因而需要获取本地电脑公钥，然后登录github账号，添加公钥至github就OK了。
 1. 设置git的user.name和user.email
 ```
 git config --global user.name "yourname"
 git config --global user.email "youremail"
 ```
 2. 查看生成的公钥文件夹
 ```
 cd ~/.ssh
 ```
 3. 生成公钥
 ```
 ssh-keygen -t rsa -c "youremail"
 ```
 得到两个文件`id_rsa`和`id_rsa.pub`
 4. 在github上添加id_rsa中的密钥
 ```
 vim id_rsa.pub
 ```
 序列码即为公钥，复制序列码，包含ssh-rsa等标识。然后登录github，进入settings--->ssh and gpg keys-->new ssh key 添加即可，其中title自行命名
 
 5. git clone
 ```
 git clone @github.com:yourname/Python.git
 ```

## git 查询用户名和密码
1. git config user.name
2. git config user.email
## git bash 提交没有绿格子问题

git bash 中的邮箱地址和github的邮箱地址不一致造成的，在git bash中将邮箱地址更改为github中的邮箱地址

```
git config --global user.email "xx@xx.com"
```

## 搭建个人博客网站
[Github pages](https://pages.github.com/)