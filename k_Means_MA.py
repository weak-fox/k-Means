import numpy as np 


class kMeans_MA:

    def __init__(self, k, times):   #k表示k个类，times表示迭代次数
        self.k = k
        self.times = times

    def train (self,X):     #X为待训练的样本数组
        X = np.asarray(X)
        np.random.seed(0)
        self.cluster_centers_=X[np.random.randint(0,len(X),self.k)]
        self.labels_ = np.zeros(len(X)) #用于储存最小距离行的索引
        for t in range(self.times):
            for index , x in enumerate(X):
                dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2/X.var(axis=0),axis = 1))   #马氏距离
                self.labels_[index] = dis.argmin()  #返回类的编号
            for i in range(self.k):# 计算每个类中所有的点，更新聚类中心点
                self.cluster_centers_[i]= np.mean(X[self.labels_ == i], axis = 0)
    
    def predict(self,X):    #X为样本数组
        X = np.asarray(X,dtype="int64")
        result = np.zeros(len(X))
        for index , x in enumerate(X):
            dis = np.sqrt(np.sum((x - self.cluster_centers_) **2/X.var(axis=0),axis = 1))
            result[index] = dis.argmin()
        return result



