import numpy as np 
import pandas as pd 
import os
import sys


list=os.listdir("./")
for i in list:
    if(i.split('.')[-1]=='xlsx'):
        data = pd.read_excel(i, index_col=0)
    elif(i.split('.')[-1]=='csv'):
        data =  pd.read_csv(i)



class kMeans_EU:

    def __init__(self, k, times):       #k表示k个类，times表示迭代次数
        self.k = k
        self.times = times

    def train (self,X):     #X为待训练的样本数组
        X = np.asarray(X)
        np.random.seed(0)
        self.cluster_centers_=X[np.random.randint(0,len(X),self.k)]
        self.labels_ = np.zeros(len(X)) #用于储存最小距离行的索引
        for t in range(self.times):
            for index , x in enumerate(X):
                dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2,axis = 1))   #欧氏距离
                self.labels_[index] = dis.argmin()  #返回类的编号
            for i in range(self.k):# 计算每个类中所有的点，更新聚类中心点
                self.cluster_centers_[i]= np.mean(X[self.labels_ == i], axis = 0)
    
    def predict(self,X):    #X为样本数组
        X = np.asarray(X)
        result = np.zeros(len(X))
        for index , x in enumerate(X):
            dis = np.sqrt(np.sum((x - self.cluster_centers_) **2,axis = 1))
            result[index] = dis.argmin()
        return result
try:
    t = data.iloc[:,:]
    kmeans = kMeans_EU(4,100)
    kmeans.train(t) #对数据进行训练
    print(t.shape)
    print(t[kmeans.labels_ == 0]) #类0中的数据
    print(kmeans.labels_)
    result=kmeans.predict(t)  #进行预测
    print(result)
except:
    print("文件不存在！")
    sys.exit()



