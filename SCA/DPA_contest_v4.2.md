## Window平台 Matlab语言 针对DPA_contest_v4.2的学习测试
### 通信协议  emmmm github仓库也可以设置为非public 好傻
攻击包装器（the attack wrapper）和攻击程序（attack program）之间的通信过程：program读取wrapper发送来的能量轨迹，
wrapper是通过FIFO（FIFO类似于一个文件，用于wrapper和attack program之间的通信）发送轨迹的，攻击程序然后通过另外一个FIFO发送结果给wrapper。

### 攻击案例
examples/v4_2/attack_windows.m，在这个文件里需要修改的是输入FIFO的名称、输出FIFO的名称、攻击的子密钥的数量
、攻击代码（共需要填写4项）

如果wrapper使用fork mode(Unix)，wrapper自己启动；windows上wrapper使用FIFO mode，wrapper会产生两个特别的文件（这个文件没有产生啊？？？）这个时候attack必须手动启动，而且必须打开这两个文件，在windows上`\\.\pipe\xxx_from_wrapper`只读模式，`\\.\pipe\xxx_to_wrapper`只写模式（能不能认真读说明文档！）

接着，从wrapper中读数据，attack program从`\\.\pipe\xxx_from_wrapper`中读，发送数据`\\.\pipe\xxx_to_wrapper`，xxx表示fifo
