## Window平台 Matlab语言 针对DPA_contest_v4.2的学习测试
### 通信协议  emmmm github仓库也可以设置为非public 好傻
攻击包装器（the attack wrapper）和攻击程序（attack program）之间的通信过程：program读取wrapper发送来的能量轨迹，
wrapper是通过FIFO（FIFO类似于一个文件，用于wrapper和attack program之间的通信）发送轨迹的，攻击程序然后通过另外一个FIFO发送结果给wrapper。
