# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import cv2
import random
import time

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

class Perceptron(object):

    def __init__(self):
        self.learning_step = 0.0001
        self.max_iteration = 5000

    def predict_(self, x):
        wx = sum([self.w[j] * x[j] for j in range(len(self.w))])
        return int(wx > 0)# if wx > 0 , return 1; else return 0
    
    def train(self, features, labels):       
        # len(features[0]) : columns 权重初始化为[0.0,...]
        self.w = [0.0] * (len(features[0]) + 1) 

        correct_count = 0
        time = 0

        while time < self.max_iteration:
            index = random.randint(0, len(labels) - 1) # 选取随机一个0到len(labels)-1的一个数
            x = list(features[index]) # 取出第index样本的特征，相对于w少一位
            #x.append(0)
            x.append(1) # 准确率更高一些
            y = 2 * labels[index] - 1 # 对原始label 1 和 0 进行处理，划分为 +1 和 -1 两个类别
            wx = sum([self.w[j] * x[j] for j in range(len(self.w))])
            
            if wx * y > 0: # 正确分类，非误分类点
                correct_count += 1
                # 正样本个数大于最大迭代数，结束循环，可以认为是对所有点都没有误分类，不再更新参数
                if correct_count > self.max_iteration: 
                    break
                continue
            
            for i in range(len(self.w)):
                self.w[i] += self.learning_step * (y * x[i]) # 把b合并到w中了，一个样本点，一个y，多维x
           
    def predict(self, features):
        labels = []
        for feature in features:
            x = list(feature)
            x.append(1)
            labels.append(self.predict_(x))
        return labels
            
if __name__ == '__main__':
    print('Start read data')

    time_1 = time.time()

    raw_data = pd.read_csv('D:\\OneDrive - ustc6\\lihang_book_algorithm\\data\\train_binary.csv', header = 0)
    data = raw_data.values # raw_data:pandas.DataFrame data:numpy array

    imgs = data[0::,1::]
    labels = data[::,0]

    #选取 2/3 数据作为训练集， 1/3 数据作为测试集
    train_X, test_X, train_Y, test_Y = train_test_split(
        imgs,labels,test_size = 0.33, random_state = 23323 )

    print(train_X.shape)

    time_2 = time.time()
    print('read date cost %f second' % (time_2 - time_1))

    print('Start training')
    p = Perceptron()
    p.train(train_X,train_Y)
 
    time_3 = time.time()
    print("train cost %f second" %(time_3 - time_2))
    
    print("Start predicting")
    test_predict_Y = p.predict(test_X)
    time_4 = time.time()
    print('training cost %f second' % (time_4 - time_3))

    score = accuracy_score(test_Y, test_predict_Y)
    print('The accuracy score is %f'  % score)
