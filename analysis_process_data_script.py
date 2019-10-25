import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import csv

data = pd.read_csv('/Users/lianxiaobao/lianxiaobao/bigdatabook/daletou2.csv')
# data = pd.read_csv('/Users/lianxiaobao/lianxiaobao/bigdatabook/daletou2.csv' ,usecols=[3,11])
# print(data.head())

print(int(data.describe().ix[0,0]))
record_num = data.__len__()
print(record_num)
print(data.ix[0, :])

# 遍历出所有行
# for i in range(record_num):
#     record = data.ix[i, :]
#     # re.sub(r'[^\w\s]', '',s) 去除逗号
#     print(re.sub(r'[^\w\s]', '', str(record['prize_pool'])))
#     print(re.sub(r'[-]', '', str(record['result_day'])))

# 去除符号
def convert1(record):
    record = re.sub(r'[^\w\s]', '', str(record))
    return record

# 去除 -
def convert2(record):
    record = re.sub(r'[-]', '', str(record))
    return record

#建新csv文件
path = r'/Users/lianxiaobao/lianxiaobao/bigdatabook/daletou4.csv'
csvfile = open(path, 'w', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(('Unnamed: 0','result_num', 'resrult_bef1', 'resrult_bef2', 'resrult_bef3', 'resrult_bef4',
       'resrult_bef5', 'resrult_beh1', 'resrult_beh2','prize_pool', 'first_prize_size', 'first_prize','second_prize_size',
        'second_prize', 'result_day','total_bet_amount'))

for i in range(record_num):
    record = data.ix[i, :]
    first_prize = int(convert1(record['first_prize']))
    prize_pool = int(convert1(record['prize_pool']))
    second_prize = int(convert1(record['second_prize']))
    # 时间类型保持不变就好 去掉-分隔符会导致py画图稀疏
    # result_day = int(convert1(record['result_day']))
    total_bet_amount = int(convert1(record['total_bet_amount']))

    writer.writerow((record['Unnamed: 0'], record['result_num'], record['resrult_bef1'], record['resrult_bef2'],
                     record['resrult_bef3'], record['resrult_bef4'], record['resrult_bef5'], record['resrult_beh1'], record['resrult_beh2']
                     , prize_pool, record['first_prize_size'], first_prize, record['second_prize_size'], second_prize, record['result_day'],
                     total_bet_amount))
csvfile.close()




 
