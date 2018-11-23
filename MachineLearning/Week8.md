<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

## Unsupervised Learning
<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k1.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k5.PNG" width="600"/> </div><br>

## Principal Component Analysis

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_1.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_5.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p5.PNG" width="600"/> </div><br>

## Programming Exercise: K-means Clustering and Principal Component Analysis
### 1.K-means Clustering
实现K-means算法用于图像压缩，先在示例2D数据集上进行实验以便很好地理解K均值算法是怎么工作的。然后，使用K-means算法通过减少图像中颜色数来进行图像压缩。

1.1 实现K-means

K-means是自动聚类相似的数据方法。具体来说，给定训练数据集 ${x^{(1)},...,x^{(m)}}$ ，其中x^{(i)}属于Rn，将数据分成几个紧密结合的“簇”。K-means是一个迭代过程，由一个猜测的初始质心，将数据分配距离最近的质心，然后重新计算质心。

算法内部循环包含两个部分：(i)分配训练数据距离最近的质心；(ii)根据分配的数重新计算质心。K均值算法需要多次初始化来选择合适的分类,选择的指标是：最低代价函数值。

1.1.1 找到最近的质心

质心的索引分配给训练数据，在计算最近距离的时候使用的是质心所在位置的数值。
`findClosestCentroids.m`这个函数的输入数据是矩阵`X`和所有质心的位置`centroids`，输出是一位矩阵`idx`保存每个训练数据距离最近的质心的索引。
```Matlab
% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%
train_num = size(X,1);
c = zeros(size(K,1),1);
for i = 1:train_num
    for j = 1:K
        c(j) = sum((X(i,:) - centroids(j,:)).^2);% compute distance return index       
    end
    idx(i) = find(c == min(c));    
end
```
1.1.2 计算质心均值
对每个点分配一个质心，算法的第二个阶段是重新计算，对于每一个质心，是所有点的均值。
$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$