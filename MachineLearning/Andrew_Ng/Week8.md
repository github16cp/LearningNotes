# Unsupervised Learning
<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k1.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8k5.PNG" width="600"/> </div><br>

# Principal Component Analysis

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_1.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p1_5.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p2.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p3.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p4.PNG" width="600"/> </div><br>

<div align="center"> <img src="https://github.com/github16cp/LearningNotes/blob/master/MachineLearning/images/w8p5.PNG" width="600"/> </div><br>

# Programming Exercise: K-means Clustering and Principal Component Analysis
## 1. K-means Clustering
将K-means算法用于图像压缩，先在示例2D数据集上进行实验以便很好地理解K均值算法是怎么工作的。然后，使用K-means算法减少图像中颜色数来进行图像压缩。

### 1.1 实现K-means

K-means是自动聚类相似数据的方法。具体来说，给定训练数据集 {x(1),...,x(m)} ，其中x(i)属于Rn，将数据分成几个紧密结合的“簇”。K-means是一个迭代过程，首先，随机初始化质心，将数据分配距离最近的质心，然后，重新计算质心。

算法内部循环包含两个部分：(i) 将训练数据分配给距离最近的质心；(ii) 根据分配的数据重新计算质心。K均值算法需要多次初始化来选择合适的分类，选择的指标是：最低代价函数值。

#### 1.1.1 找到最近的质心

将质心的索引分配给训练数据，在计算最近距离的时候使用的是质心所在位置的数值。

`findClosestCentroids.m`这个函数的输入数据是矩阵`X`和所有质心的位置`centroids`，输出是一个列向量`idx`，它保存了每个训练数据距离最近的质心的索引。
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
for i = 1:size(X,1)
    cluster = zeros(K,1);% 这句放在外边有点问题
    for j = 1:K        
        cluster(j) = sum((X(i,:) - centroids(j,:)).^2); 
    end
    idx(i) = find(cluster == min(cluster));
end
```
#### 1.1.2 计算质心均值

对每个样本分配一个质心，算法第二部重新计算质心，对于每一个质心，他的值是所有离它最近的点（分配给它的数据）的均值。

`computeCentroids.m`
```Matlab
% 如何进行向量化的实现
for i = 1:K
    class_i = find(idx == i);
    centroids(i,:) = 1/size(class_i,1)*sum(X(class_i,:));
end

```
### 1.2 在示例数据集上运用K-means

### 1.3 随机初始化
在选择初始质心位置时，不合适的质心会产生不好的聚类结果，进行多次随机选择，选取最好的聚类结果的质心。
```Matlab
% Randomly recorder the indices of examples
randidx = randperm(size(X,1));

% Take the first K examples as centroids

centroids = X(randidx(1:K),:)
```

### 1.4 使用K-means进行图像压缩

一个图像用24位的颜色表示，每一个像素表示成3个8bit的无符号整数（0-255），分别表示red，green，blue密度值，这种编码方式叫做RGB编码方式。图像包含了成千上百个颜色，目标：将图像颜色数减少，减少为16色。

为了完成这种缩减，只需要存储16个选择颜色的RGB的值，每个像素点只需要存储对应位置颜色的索引（4bit足够表示16个颜色值）。

使用K-means方法选择16色来表示压缩图像，将原始图像的每一个像素点看作是数据样本并使用K-means算法在3维RGB空间中找到像素最好的16个分类。一旦计算出图像的簇质心，就用这16色替换原来图像的像素。

## 2. Principal Component Analysis

### 2.1 示例数据集
一个2D数据，在一个方向上有较大的方差，另外一个方向上有较小的方差。当用PCA将这个2D数据降为1D时，会发生什么呢？
### 2.2 实现PCA

PCA包含两个计算步骤：第一步，计算数据的协方差；第二步，使用Matlab的SVD函数计算特征向量（计算协方差矩阵的特征向量）U1,U2,...,Un，这些特征向量对应着数据的主成分。

在使用PCA之前需要将数据进行标准化,对数据的每个维度进行scale使得他们在同一个范围内。

计算主成分：
```Matlab
sigma = 1/m*X'*X;
[U, S, V] = svd(sigma);
```
其中，X表示数据矩阵，每一行表示一个样本，m是样本的数量，`sigma`表示协方差矩阵，是一个n*n的矩阵，而不是求和算子（和求和符号长的有点像）。接着，对这个协方差矩阵进行`svd`分解，结果U包含了主成分，S是一个对角矩阵，对角元素是特征值。

最大的特征向量（对应着最大的特征值）是top主成分。

输入数据X（m*n：50*2），50：样本数量，n：特征数量，U：2*2，top特征向量:第一个特征向量：U(:,1)

### 2.3 使用PCA进行维度约减

计算主成分之后，使用主成分减少特征维度通过将样本投影到一个低维空间中。

#### 2.3.1 将数据投影到主成分上

```Matlab
U_reduce = U(:,1:K);
Z = X*U_reduce;
```

#### 2.3.2 重构数据（近似数据）

原始数据投影到低维空间，如果要恢复原始数据的话，可以通过投影回来到原始的高维空间来近似恢复原始数据。

```Matlab
U_reduce = U(:,1:K);
X_rec = Z*U_reduce';

```

#### 2.3.3 可视化投影
投影仅仅保留了在U1方向上的信息。

### 2.4 脸部图像数据集

在实际中应用PCA，现有脸部图像数据集X，每个图是32*32的灰度图，每行代表一个图片，长度为1024的向量。

#### 2.4.1 应用PCA
将数据集标准化，应用PCA，获取主成分，U的每行是一个长度为n的向量（n=1024），将这些主成分重新排列成一个32*32的矩阵对应于原来图像的每个像素。

#### 2.4.2 维度缩减
将原来的数据集投影到前100个主成分上，每个图像由一个100个特征的向量表示。

恢复的数据集与原来的数据集相比，丢失了不少的信息，由此可以看出，PCA在提升学习效率方面的重要性。

### 2.5 PCA用于可视化
3D看起来麻烦，用2D进行可视化，PCA投影可以看作是一个旋转，选择一个视角最大化数据传播。