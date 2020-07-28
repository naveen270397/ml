import numpy as np
import pandas as pd
import csv
import random
from sklearn.cluster import KMeans
def rand (start , end , count ):
    res=[];
    for i in range(count):
        res.append(random.randint(start, end));
    return res;

def main():

    #transactions = [[1, 2, 5],[2, 4],[2, 3],[1, 2, 4],[1, 3],[2, 3],[1, 3],[1, 2, 3, 5],[1, 2, 3]]

    tableId=rand(1,100,1000);
    userId1=rand(1,25,500);
    userId2=rand(10,40,500);
    userId=userId1+userId2;
    ip=[200 for x in range(1000)]
    after_dec1=rand(100,150,400);
    after_dec2=rand(150,999,600);
    after_dec=after_dec1+after_dec2;
    after_dec=[x/1000 for x in after_dec]
    #ip=[float(x) for x in ip]
    for item in range (1000):
        ip[item]=ip[item]+after_dec[item]
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
if __name__ == "__main__":
    main();
