## Window平台 Matlab语言 针对DPA_contest_v4.2的学习测试
### 通信协议  emmmm github仓库也可以设置为非public 好傻
攻击包装器（the attack wrapper）和攻击程序（attack program）之间的通信过程：program读取wrapper发送来的能量轨迹，
wrapper是通过FIFO（FIFO类似于一个文件，用于wrapper和attack program之间的通信）发送轨迹的，攻击程序然后通过另外一个FIFO发送结果给wrapper。

### 攻击案例
examples/v4_2/attack_windows.m，在这个文件里需要修改的是输入FIFO的名称、输出FIFO的名称、攻击的子密钥的数量
、攻击代码（共需要填写4项）

如果wrapper使用fork mode(Unix)，wrapper自己启动；windows上wrapper使用FIFO mode，wrapper会产生两个特别的文件（这个文件没有产生啊？？？）这个时候attack必须手动启动，而且必须打开这两个文件，在windows上`\\.\pipe\xxx_from_wrapper`只读模式，`\\.\pipe\xxx_to_wrapper`只写模式（能不能认真读说明文档！）

接着，从wrapper中读数据，attack program从`\\.\pipe\xxx_from_wrapper`中读，发送数据`\\.\pipe\xxx_to_wrapper`，xxx表示fifo


选择v4_2死活不成功，选择256bit的成功了

首先在windows命令提示符界面输入
```
D:\attack_wrapper-2.2.0>attack_wrapper -d DPA_contestv4_rsm -x dpav4_rsm_index -e v4_RSM fifo
D - Output filename = results (abort if exists)
D - FIFO mode
D - Base name for FIFOs = fifo
D - Compatibility mode (v2) = disabled
D - Traces will be read from directory DPA_contestv4_rsm
D - Using index file dpav4_rsm_index
D - We will check if traces are available
D - Offsets are not provided to the attack
I - Reading index file...
D - Total number of traces in the index file = 6
D - Total number of traces available = 6
D - Total number of keys in the index file = 1
D - Total number of keys available = 1
D - Key #00 (6cecc67f287d083deb8766f0738b36cf164ed9b246951090869d08285d2e193b): 6 traces available
D - Key # = 0
D - # of traces = 6
I - Preparing the results file...
I - FIFO Wrapper -> Attack: \\.\pipe\fifo_from_wrapper
I - FIFO Attack -> Wrapper: \\.\pipe\fifo_to_wrapper
I - Sending # of iterations (6)
I - The attack is ready!
```
停止在这个界面，然后再matlab中命令行输入
```
attack_windows
```
然后在命令行提示符界面看到以下结果
```
I - Trace #000000: Reading trace / Sending trace / Waiting for results / Saving results / Done (9.6 s) [                ]
I - Trace #000001: Reading trace / Sending trace / Waiting for results / Saving results / Done (9.1 s) [                ]
I - Trace #000002: Reading trace / Sending trace / Waiting for results / Saving results / Done (9.0 s) [                ]
I - Trace #000003: Reading trace / Sending trace / Waiting for results / Saving results / Done (9.2 s) [                ]
I - Trace #000004: Reading trace / Sending trace / Waiting for results / Saving results / Done (9.7 s) [                ]
I - Trace #000005: Reading trace / Sending trace / Waiting for results / Saving results / Done (10.1 s) [                ]
I - Closing the results file...
I - FIFOs closed
```
生成一个result文件，用记事本打开是乱码，这个时候就需要官网自带的结果分析工具对结果进行分析，这个分析工具用来计算不同的评价指标
```
D:\attack_wrapper-2.2.0>compute_results.exe results
I - Open file results
II - Compute result metrics
II - Writing result files
```
