import numpy as np 
import pandas as pd 
import os
import sys
from k_Means_MA import kMeans_MA


list=os.listdir("./predict_data")
for i in list:
    if(i.split('.')[-1]=='xlsx'):
        data = pd.read_excel("./predict_data/"+i, index_col=0,)
    elif(i.split('.')[-1]=='csv'):
        data =  pd.read_csv("./predict_data/"+i)



try:
    #####K-Means算法的应用2：通过输入文档里的数据对输入的单挑数据进行分类####
    print("---------------------------------------------")
    print("输入前请确认需要的文件已放在k-Means/predict_data目录下！！！")
    k=input("请输入分类个数:")
    k=int(k)
    times=input("请输入迭代次数:")
    times=int(times)
    t = data.iloc[:,:]
    kmeans = kMeans_MA(k,times)
    kmeans.train(t) #对数据进行训练
    print("数据训练完成!")
    input=input("请输入需要预测的数据（数据之间用逗号隔开）:")
    t1 = input.split(",")           #字符串转化为int型的list
    for i in range(len(t1)):        
        t1[:][i]=int(t1[:][i])
    t1=[t1]                     
    result=kmeans.predict(t1)  #进行预测
    print("输入数据所属的类为：")
    print(int(result[0]))   #输出结果
    i=int(result[0])
    print("类"+str(i)+":")
    print(t[kmeans.labels_ == i])
    print("      类"+str(i))

    print("---------------------------------------------")
except:
    print("文件不存在！请打开整个文件夹运行！")
    sys.exit()