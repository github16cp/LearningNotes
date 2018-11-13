### 常见Error及解决方法汇总
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
