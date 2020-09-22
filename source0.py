import numpy as np
import pandas as pd
import csv
import random
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
def repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

def rand (start , end , count ):
    res=[];
    for i in range(count):
        res.append(random.randint(start, end));
    return res;
def main():
    userId=[];
    for item in range(1000):
        userId.append(item);
    ip=[200 for x in range(1000)];
    after_dec1=rand(0,999,1000)
    after_dec=after_dec1;
    after_dec=[x/1000 for x in after_dec]
    for item in range (1000):
        ip[item]=ip[item]+after_dec[item]
    with open('name_data.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for item in range(1000):
        data[item].append(userId[item]);
        data[item].append(ip[item]);
        data[item].append(0);

    new_ips=repeat(ip);

    for item in range(0, len(new_ips)):
        for nest in range(0,1000):
            if data[nest][4]==new_ips[item]:
                data[nest][5]=1111
                data[nest][0]="fname"+str(new_ips[item]);

    for item in range(0,int (len(new_ips))):
        count=0;
        for nest in range(0,1000):
            if data[nest][4]==new_ips[item] and count<2:
                data[nest][5]=22222
                data[nest][1]="lname"+str(new_ips[item]);
                count+=1;

    for item in range(0,int (len(new_ips))):
        count=0;
        for nest in range(0,500):
            if data[nest][4]==new_ips[item] and count<2:
                data[nest][5]=333333
                data[nest][2]="passwdip"+str(new_ips[item]);
                count+=1;

    with open("createddata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    newdata=[[data[val][3],data[val][5]] for val in range(1000)];
    kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=30, n_init=10, random_state=0);
    pred_y = kmeans.fit_predict(newdata)
    #   print(pred_y);
    #print("centroids: ", kmeans.cluster_centers_)
    #print("labels: ", kmeans.labels_)
    my_dict = {kmeans.cluster_centers_[i, 0]: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
    print(my_dict)

    for item in range(1000):
        data[item].append(0);
        data[item].append(0);
        data[item].append(0);
        data[item].append(0);
    for item in range(1000):
        if data[item][5]==0:
            data[item][6]=1
    for item in range(1000):
        if data[item][5]==1111:
            data[item][7]=25
    for item in range(1000):
        if data[item][5]==22222:
            data[item][8]=50
    for item in range(1000):
        if data[item][5]==333333:
            data[item][9]=75
#    for item in range(1000):
#        print(data[item]);
    x1_train=[];
    y1_train=[];
    x2_train=[];
    y2_train=[];
    x3_train=[];
    y3_train=[];
    x4_train=[];
    y4_train=[];
    for item in range(1000):
        x1_train.append(data[item][5])
        y1_train.append(data[item][6])
    for item in range(1000):
        x2_train.append(data[item][5])
        y2_train.append(data[item][7])
    for item in range(1000):
        x3_train.append(data[item][5])
        y3_train.append(data[item][8])
    for item in range(1000):
        x4_train.append(data[item][5])
        y4_train.append(data[item][9])

    for item in range(1000):
        if (x2_train[item]!=1111):
            x2_train[item]=0;
        if (x3_train[item]!=22222):
            x3_train[item]=0;
        if (x4_train[item]!=333333):
            x4_train[item]=0;
    logisticRegr1 = LogisticRegression()
    logisticRegr1.fit(np.array(x1_train).reshape(-1,1), y1_train)
    logisticRegr2 = LogisticRegression()
    logisticRegr2.fit(np.array(x2_train).reshape(-1,1), y2_train)
    logisticRegr3 = LogisticRegression()
    logisticRegr3.fit(np.array(x3_train).reshape(-1,1), y3_train)
    logisticRegr4 = LogisticRegression()
    logisticRegr4.fit(np.array(x4_train).reshape(-1,1), y4_train)

    x_test=[str(x) for x in input().split()];
    x_test[3]=int(x_test[3])
    x_test[4]=float(x_test[4])
    x_test.append(0);
    for item in range(1000):
        if data[item][0]==x_test[0]:
            x_test[5]=1111;
    for item in range(1000):
        if data[item][0]==x_test[0] and data[item][1]==x_test[1]:
            x_test[5]=22222;
    for item in range(1000):
        if data[item][0]==x_test[0] and data[item][1]==x_test[1]:
            if data[item][2]==x_test[2]:
                x_test[5]=333333;


#    print(x_test);
    test_x=np.array(x_test[5]);
#    print(test_x);
    predictions1 = logisticRegr1.predict(test_x.reshape(-1,1));
    print(predictions1/100);
    predictions2 = logisticRegr2.predict(test_x.reshape(-1,1));
    print(predictions2/100);
    predictions3 = logisticRegr3.predict(test_x.reshape(-1,1));
    print(predictions3/100);
    predictions4 = logisticRegr4.predict(test_x.reshape(-1,1));
    print(predictions4/100);
if __name__=="__main__":
    main();
