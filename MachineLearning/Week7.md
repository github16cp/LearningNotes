### SVM分类器

用SMO算法训练一个SVM分类器，ex6用一个简化版本的SMO训练一个分类器，推荐更多优化包：[LIBSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/)(高度优化的SVM工具箱)、[SVMLight](http://svmlight.joachims.org/)

查看一下SMO算法是否与`ex6`的`svmTrain.m`对应的上

应用算法学习到的参数保存到模型中:
```
% Save the model
idx = alphas > 0;
model.X= X(idx,:);
model.y= Y(idx);
model.kernelFunction = kernelFunction;
model.b= b;
model.alphas= alphas(idx);
model.w = ((alphas.*Y)'*X)';
```

SVM学习到一个非线性的决策边界，根据model画出来这个决策边界，`visualizeBoundary`

### 2 垃圾邮件分类
2.1 预处理邮件
* 将邮件内容转换为小写字母

2.2 从邮件中获取特征
首先将每个邮件转换为n维的向量，n等于词汇表中单词的数量。特征 x_i 表示词汇表中的第i单词是否出现在邮件中，出现：x_i = 1，否则 x_i = 0

2.3 为垃圾邮件分类训练SVM
训练集准确性：99.8%， 测试集准确性：98.5%

2.4 Top Predictors for Spam（垃圾邮件最高预测因子）

### 选做题
自己的数据集：[SpamAssassin Public Corpus](http://spamassassin.apache.org/old/publiccorpus/)
