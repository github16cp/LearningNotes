### SVM分类器

用SMO算法训练一个SVM分类器，ex6用一个简化版本的SMO训练一个分类器，推荐更多优化包：[LIBSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/)、[SVMLight](http://svmlight.joachims.org/)

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
