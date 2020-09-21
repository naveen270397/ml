import numpy as np
import pandas as pd
import csv
import random
from sklearn.cluster import KMeans
import pyfpgrowth
def fp1(userId,tableId):
    data=[[userId[val],tableId[val]] for val in range(1000)];
    transactions =[];
    inner=[]
    for i in range(1,101):
        for j in range(len(data)):
            if data[j][1]==i:
                inner.append(data[j][0]);
        transactions.append(inner);
        inner=[]
    print(transactions)
    patterns = pyfpgrowth.find_frequent_patterns(transactions, 5);
    for keys,values in patterns.items():
        print(keys,"      ",values )
def fp2(userIds,tableId,result):
    for item in range(len(userIds)):
        if (item%3==0):
            userIds[item]=str(userIds[item])+result[item]
        else:
            userIds[item]=str(userIds[item])+result[item]
    data=[[userIds[val],tableId[val]] for val in range(1000)];
    transactions =[];
    inner=[]
    for i in range(1,101):
        for j in range(len(data)):
            if data[j][1]==i:
                inner.append(data[j][0]);
        transactions.append(inner);
        inner=[]
    patterns = pyfpgrowth.find_frequent_patterns(transactions, 5);
    for keys,values in patterns.items():
        print(keys,"            ",values )

def km(userId,tableId,ip):
    for item in range(len(ip)):
         if ip.count(ip[item])>7:
             ip[item]=ip[item]/100
             print(item)
    data=[[userId[val],tableId[val],ip[val]] for val in range(1000)];
    kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=20, n_init=10, random_state=0);
    pred_y = kmeans.fit_predict(data)
    #   print(pred_y);
    #print("centroids: ", kmeans.cluster_centers_)
    #print("labels: ", kmeans.labels_)
    my_dict = {kmeans.cluster_centers_[i, 0]: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
    print(my_dict)

def rand (start , end , count ):
    res=[];
    for i in range(count):
        res.append(random.randint(start, end));
    return res;
def main():
    tableId=rand(1,100,1000);
    userId1=rand(1,25,500);
    userId2=rand(15,40,500);
    userId=userId1+userId2;
    result=[]
    for item in range (1000):
        if (item%3==0):
            result.append("w");
        else:
            result.append("l");
    ip=[200 for x in range(1000)]
    after_dec1=rand(100,150,400);
    after_dec2=rand(150,999,600);
    after_dec=after_dec1+after_dec2;
    after_dec=[x/1000 for x in after_dec]
    for item in range (1000):
        ip[item]=ip[item]+after_dec[item]
    data=[[userId[val],tableId[val],result[val],ip[val]] for val in range(1000)];
    with open("game_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    while(1):
        print("1. always playing together ")
        print("2. winning / loosing  ")
        print("3. different players using same Ip ")
        inp=input ("enter choice");
        if inp=="1":
            fp1(userId,tableId);
        if inp=="2":
            fp2(list(userId),tableId,result);
        if inp=="3":
            km(userId,tableId,ip);

if __name__ == "__main__":
    main();
