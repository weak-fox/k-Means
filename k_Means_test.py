import numpy as np 
import pandas as pd 
import os
import sys
from k_Means_MA import kMeans_MA


list=os.listdir("./test_data")
for i in list:
    if(i.split('.')[-1]=='xlsx'):
        data = pd.read_excel("./test_data/"+i, index_col=0,)
    elif(i.split('.')[-1]=='csv'):
        data =  pd.read_csv("./test_data/"+i)



try:
    ###K-Means算法的应用1：对输入文档里的数据进行分类###
    print("---------------------------------------------")
    print("输入前请确认需要的文件已放在k-Means目录下！！！")
    k=input("请输入分类个数：")
    k=int(k)
    t = data.iloc[:,:]
    kmeans = kMeans_MA(k,100)#进行100次迭代
    kmeans.train(t) #对数据进行训练
    # print(t.shape)
    # print(kmeans.labels_)
    # result=kmeans.predict(t)  #进行预测
    # print(result)#结果顺序按每个标签
    for i in range(kmeans.k):
        print("类"+str(i)+":")
        print(t[kmeans.labels_ == i]) #类i中的数据
    print("类0 ~ 类"+str(k-1)+"  共"+str(k)+"个类")
    print("---------------------------------------------")
except:
    print("文件不存在！请打开整个文件夹运行！")
    sys.exit()