## Window平台 Matlab语言 针对DPA_contest_v4.2的学习测试
### 通信协议
攻击包装器（the attack wrapper）和攻击程序（attack program）之间的通信过程：attack program读取wrapper通过FIFO（FIFO类似于一个文件，用于wrapper和attack program之间的通信）发送来的能量轨迹，攻击程序然后通过另外一个FIFO发送结果给wrapper。

在这个过程中，首先先在windows命令提示符中启动wrapper，然后手动在matlab中启动attack program。

### 攻击案例
examples/v4_2/attack_windows.m，在这个文件里需要修改的是输入FIFO的名称、输出FIFO的名称、攻击的子密钥的数量
、攻击代码（共需要填写4项）

如果wrapper使用fork mode(Unix)，wrapper自己启动；windows上wrapper使用FIFO mode，wrapper会产生两个特别的文件，这个时候attack必须手动启动，而且必须打开这两个文件，在windows上`\\.\pipe\xxx_from_wrapper`只读模式，`\\.\pipe\xxx_to_wrapper`只写模式

接着，从wrapper中读数据，attack program从`\\.\pipe\xxx_from_wrapper`中读，发送数据`\\.\pipe\xxx_to_wrapper`，xxx表示fifo，即命令的最后一个参数

但是在具体实验的过程中，选择v4_2版本的数据集，即128bit的AES掩码方案的实现的能量轨迹，实验并不成功。

于是，改变数据集，也是很无奈啊，使用DPA_contestv4_rsm数据集，从官网上下载的0-9999一共1w条轨迹，在读取的时候只使用了0-5个（单单为了测试tools能不能用）

测试步骤如下：

1. 首先在windows命令提示符界面输入
```
D:\attack_wrapper-2.2.0>attack_wrapper -d DPA_contestv4_rsm -x dpav4_rsm_index -e v4_RSM fifo
```
`-d`：轨迹的所在目录

`-x`: index file

`-e`: 数据集版本

最后一个参数：`fifo`, 在windows中wrapper和attack的通信方式是fifo

2. 显示结果
```
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
**v4_2应该也是可行的，是不是因为解压了轨迹的原因**

3. matlab中命令行输入
```
attack_windows
```
4. 然后在命令行提示符界面看到以下结果
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
此时生成一个result文件，用记事本打开是乱码，这个时候就需要官网自带的结果分析工具对结果进行分析，这个分析工具用来计算不同的评价指标
5. 使用compute_results
```
D:\attack_wrapper-2.2.0>compute_results.exe results
I - Open file results
II - Compute result metrics
II - Writing result files
```
results文件的名字可以在开始指定，目录下多出了很多的文件，打开其中一个`results_global_success_rate.dat`，显示结果如下
```
# Trace_num Global_success_rate
0 0.000000
1 0.000000
2 0.000000
3 0.000000
4 0.000000
5 0.000000
```
分析对于v4_2错误的原因：轨迹文件解压之后，保持原来的文件名不变，即k00，trc.bz2文件不用解压缩，再次测试

测试结果：
```
D:\ML-SCA\SCA\DPA_traces\attack_wrapper-2.2.0>attack_wrapper -i 5 -d D:\ML-SCA\SCA\DPA_traces\DPA_contestv4_2 -x D:\ML-SCA\SCA\DPA_traces\dpav4_2_index -e v4_2 fifo
D - Output filename = results (abort if exists)
D - FIFO mode
D - Base name for FIFOs = fifo
D - Compatibility mode (v2) = disabled
D - Traces will be read from directory D:\ML-SCA\SCA\DPA_traces\DPA_contestv4_2
D - Using index file D:\ML-SCA\SCA\DPA_traces\dpav4_2_index
D - We will check if traces are available
D - Offsets/Shuffles are not provided to the attack
D - Samples are transfered as floats
I - Reading index file (v4_2)...
D - Total number of traces in the index file = 5
D - Total number of traces available = 5
D - Total number of keys in the index file = 1
D - Total number of keys available = 1
D - Key #00 (8249ceb658c71d41d7b734449629ab97): 5 traces available
D - Key # = 0
D - # of traces = 5
I - Preparing the results file...
I - FIFO Wrapper -> Attack: \\.\pipe\fifo_from_wrapper
I - FIFO Attack -> Wrapper: \\.\pipe\fifo_to_wrapper
I - Sending # of iterations (5)
I - The attack is ready!
I - Trace #000000: Reading trace / Sending trace / Waiting for results / Saving results / Done (251.9 s) [                ]
I - Trace #000001: Reading trace / Sending trace / Waiting for results / Saving results / Done (249.4 s) [                ]
I - Trace #000002: Reading trace / Sending trace / Waiting for results / Saving results / Done (249.6 s) [                ]
I - Trace #000003: Reading trace / Sending trace / Waiting for results / Saving results / Done (249.7 s) [                ]
I - Trace #000004: Reading trace / Sending trace / Waiting for results / Saving results / Done (1129.2 s) [                ]
I - Closing the results file...
I - FIFOs closed
```
此时显示可以成功读取能量轨迹
-------
目标实现SVM的攻击，距离目标还是好远好远啊
