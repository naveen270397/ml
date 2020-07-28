import csv
import random
import pyfpgrowth
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
    data=[[userId[val],tableId[val]] for val in range(1000)];
    #with open("game_data.csv", "w", newline="") as f:
    #    writer = csv.writer(f)
    #    writer.writerows(data)
    transactions =[];
    inner=[]
    for i in range(1,101):
        for j in range(len(data)):
            if data[j][1]==i:
                inner.append(data[j][0]);
        transactions.append(inner);
        inner=[]
    patterns = pyfpgrowth.find_frequent_patterns(transactions, 4);
    for keys,values in patterns.items():
        print(keys,"      ",values )


if __name__ == "__main__":
    main();
