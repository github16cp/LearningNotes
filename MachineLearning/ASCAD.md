# Study of Deep Learning Techniques for Side-Channel Analysis and Introduction to ASCAD Database 阅读笔记
## HDF5 file
[Core concepts](http://docs.h5py.org/en/stable/quick.html)

## keras.optimizers.RMSprop
[optimizers](https://keras.io/optimizers/)

优化器是编译Keras所需要的2个参数之一，优化器有：SGD、RMSprop、Adagrad、Adadelta、Adam、Adamax、Nadam。
```Python
keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
```

* epsilon: 模糊因子
* decay: 每次更新学习速率的衰减

RMSprop优化器：root mean square prop，除了学习速率之外，其余参数推荐采用优化器的默认值，RNN网络使用这个优化器是个很好的选择。

[参考笔记](https://songapore.github.io/2018/04/30/course2-Week2-7-RMSProp/)

[参考1](https://blog.csdn.net/u010089444/article/details/76725843)

[参考2](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)

RMSprop Source:
```Python
class RMSprop(Optimizer):
    """RMSProp optimizer.
    It is recommended to leave the parameters of this optimizer
    at their default values
    (except the learning rate, which can be freely tuned).
    This optimizer is usually a good choice for recurrent
    neural networks.
    # Arguments
        lr: float >= 0. Learning rate.
        rho: float >= 0.
        epsilon: float >= 0. Fuzz factor. If `None`, defaults to `K.epsilon()`.
        decay: float >= 0. Learning rate decay over each update.
    # References
        - [rmsprop: Divide the gradient by a running average of its recent magnitude
           ](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)
    """

    def __init__(self, lr=0.001, rho=0.9, epsilon=None, decay=0.,
                 **kwargs):
        super(RMSprop, self).__init__(**kwargs)
        with K.name_scope(self.__class__.__name__):
            self.lr = K.variable(lr, name='lr')
            self.rho = K.variable(rho, name='rho')
            self.decay = K.variable(decay, name='decay')
            self.iterations = K.variable(0, dtype='int64', name='iterations')
        if epsilon is None:
            epsilon = K.epsilon()
        self.epsilon = epsilon
        self.initial_decay = decay

    @interfaces.legacy_get_updates_support
    def get_updates(self, loss, params):
        grads = self.get_gradients(loss, params)
        accumulators = [K.zeros(K.int_shape(p), dtype=K.dtype(p)) for p in params]
        self.weights = accumulators
        self.updates = [K.update_add(self.iterations, 1)]

        lr = self.lr
        if self.initial_decay > 0:
            lr = lr * (1. / (1. + self.decay * K.cast(self.iterations,
                                                      K.dtype(self.decay))))

        for p, g, a in zip(params, grads, accumulators):
            # update accumulator
            new_a = self.rho * a + (1. - self.rho) * K.square(g)
            self.updates.append(K.update(a, new_a))
            new_p = p - lr * g / (K.sqrt(new_a) + self.epsilon)

            # Apply constraints.
            if getattr(p, 'constraint', None) is not None:
                new_p = p.constraint(new_p)

            self.updates.append(K.update(p, new_p))
        return self.updates

    def get_config(self):
        config = {'lr': float(K.get_value(self.lr)),
                  'rho': float(K.get_value(self.rho)),
                  'decay': float(K.get_value(self.decay)),
                  'epsilon': self.epsilon}
        base_config = super(RMSprop, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
```
## keras.callbacks.ModelCheckpoint
```Python
keras.callbacks.ModelCheckpoint(filepath, monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)
```

该函数在每个epoch后将模型保存到filepath中

* save_best_only：当设置为True时，将只保存在验证集上性能最好的模型

## keras.layers.Dense
Dense就是普通的全连接层
```Python
keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
```
`Dense`实现`output = activation(dot(input, kernel) + bias)`，其中`activation`是按照逐个元素计算的激活函数，`kernel`是由网络层创建的权值矩阵，`bias`表示偏置向量。

* units: 正整数，输出空间的维度

**输入尺寸**

`(batch_size,input_dim)`2D输入

**输出尺寸**
`(batch_size,input_dim)`2D的输入，输出为`(batch_size, units)`

## keras.models.Model
Model 模型方法

```Python
compile(self, optimizer, loss, metrics=None, loss_weights=None, sample_weight_mode=None, weighted_metrics=None, target_tensors=None)
```
`compile`函数编译模型以供训练

## fit
```Python
fit(self, x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None)
```
## Conv1D
```Python
keras.layers.Conv1D(filters, kernel_size, strides=1, padding='valid', data_format='channels_last', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
```
* filter: 输出空间的维度，在卷积中输出过滤器的数目
* kernel_size:一个整数的元组或者列表，指明了1D卷积窗口的长度

## MaxPooling1D
```Python
keras.layers.MaxPooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last')
```
## Flatten
```Python
keras.layers.Flatten(data_format=None)
```
亚平，平移输入，不影响batch_size的大小

[参考](https://keras-cn.readthedocs.io/en/latest/layers/core_layer/)

## Model类
给定输入张量和输出张量，可以实例化一个Model:
```Python
model = Model(inputs=a, outputs=b)
```
这个模型包含从`a`到`b`所有网络层。

[参考](https://keras.io/zh/models/model/)