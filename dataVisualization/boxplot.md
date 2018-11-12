### 介绍
箱线图（boxplot），又称盒须图、盒式图、箱线图，用于显示数据分散情况的统计图，它利用数据中的五个统计量：最小值，最大值，中位数，第一四分位数，第三四分位数来描述数据。
### boxplot的绘制步骤
1. 画数轴
2. 画矩形盒，矩形盒两边分别对应数据的两个四分位数（Q1和Q3），在矩形盒的内部中位数位置附近画一条黑色的条带。
3. 在Q3+1.5xIQR（IQR表示四分位距）和Q1-1.5xIQR这两处的位置画一条与中位数位置一样的线段，这两个线段表示异常值（outliers）截断点，这两个线段位置表示的是最大非异常值和最小非异常值，两者之间称为內限；在Q3+3xIQR和Q3-3xIQR处画两条线段，称其为外限。处于內限以外的都是异常值，在內限与外限之间的异常值为温和异常值（mild outliers），在外限之外的都是极端异常值（extreme outliers）。
<p align="center">
    <img src="https://github.com/github16cp/CS_Notes/blob/master/dataVisualization/boxplot1.jpg" alt="Sample"  width="550" height="400">
</p>

<p align="center">
    <img src="https://github.com/github16cp/CS_Notes/blob/master/dataVisualization/boxplot2.jpg" alt="Sample"  width="550" height="400">
</p>
### 箱线图的功能
1. 直观显示数据中的异常值；
2. 判断数据的偏态和尾重：异常值出现在一侧；中位数偏离四分位数的中心位置；
3. 数据的形状：分散还是集中，盒子长度较短较为集中；
### 缺点
箱线图不能提供数据偏态和尾重的精确度量；大量数据反应信息较为模糊；利用中位数表示总体水平太过局限。

箱线图结合其他**统计工具**比如：均值、标准差、偏度、分布函数来描述数据的分布。
