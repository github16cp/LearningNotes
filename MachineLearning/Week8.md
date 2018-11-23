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
`computeCentroids.m`
```Matlab
% 如何进行向量化的实现
for i = 1:K
    class_i = find(idx == i);
    centroids(i,:) = 1/size(class_i,1)*sum(X(class_i,:));
end

```
1.2 K-means on example dataset

plot测试

1.3 Random initialization
```Matlab
% Randomly recorder the indices of examples
randidx = randperm(size(X,1));

% Take the first K examples as centroids

centroids = X(randidx(1:K),:)
```

1.4 Image compression with K-means

（24位色）一个图像用24位的颜色表示，每一个像素表示成3个8bit的无符号整数（0-255），分别表示red，green，blue密度值，这种编码方式叫做RGB编码方式。图像包含了成千上百个颜色，目标：将颜色数减为16色。

为了完成这种缩减，只需要存储16个选择颜色的RGB的值，每个像素点只需要存储对应位置颜色的索引（4bit足够表示16个颜色值）

使用K-means方法选择16个颜色来表示压缩图像，将原始图像的每一个像素点看作是数据样本并使用K-means算法找到16个颜色在3维RGB空间中找到像素最好的分类。一旦计算出图像的簇质心，就用这16个颜色替换原来图像的像素。

### 2. Principal Component Analysis

2.1 示例数据集
2.2 Implementaing PCA

PCA包含两个计算步骤:第一步，计算数据的协方差；第二步，使用Matlab的SVD函数计算特征向量（计算协方差矩阵的特征向量），这些特征向量对应着数据的主成分。

在使用PCA之前需要将数据进行标准化。

计算主成分：
```Matlab
sigma = 1/m*X'*X;
[U, S, V] = svd(sigma);
```
2.3 使用PCA进行维度约减

计算主成分之后，使用主成分减少特征维度通过将样本投影到一个低维空间中。

2.3.1 将数据投影到主成分上

```Matlab
U_reduce = U(:,1:K);
Z = X*U_reduce;
```

2.3.2 Reconstructing an approximation of Data

数据投影到低维空间，可以近似恢复数据通过投影回来到原始的高维空间
```Matlab
U_reduce = U(:,1:K);
X_rec = Z*U_reduce';

```

2.4 脸部图像数据集
32*32的灰度图，每行长度为1024的向量