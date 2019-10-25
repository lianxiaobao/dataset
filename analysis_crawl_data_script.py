import requests
from lxml import etree
import pandas as pd


def get_ten_years_data(url):
    headers={
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

    }

    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


url="http://datachart.500.com/dlt/history/newinc/history.php?start=00001&end=19119";
# print(get_ten_years_data(url))
data = etree.HTML(get_ten_years_data(url))
# print(data)
trs = data.xpath('//tr')
k=0
for tr in trs:
    k=k+1
print(k)

/Users/lianxiaobao/lianxiaobao/lianxi_card_manage/venv/card/shishicai_analysis/analysis.py
requests =[]
for i in range(1, k-3):

    result_num = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[1]/text()')[0]
    print(result_num, end='\t')
    resrult_bef1 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[2]/text()')[0]
    print(resrult_bef1, end='\t')
    resrult_bef2 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[3]/text()')[0]
    print(resrult_bef2, end='\t')
    resrult_bef3 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[4]/text()')[0]
    print(resrult_bef3, end='\t')
    resrult_bef4 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[5]/text()')[0]
    print(resrult_bef4, end='\t')
    resrult_bef5 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[6]/text()')[0]
    print(resrult_bef5, end='\t')
    resrult_beh1 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[7]/text()')[0]
    print(resrult_beh1, end='\t')
    resrult_beh2 = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[8]/text()')[0]
    print(resrult_beh2, end='\t')
    prize_pool = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[9]/text()')[0]
    print(prize_pool, end='\t')
    first_prize_size = data.xpath('//*[@id="tdata"]/tr[' + str(i) + ']/td[10]/text()')[0]
    print(first_prize_size, end='\t')
    first_prize = data.xpath('//*[@id="tdata"]/tr[' + str(i) + ']/td[11]/text()')[0]
    print(first_prize, end='\t')
    second_prize_size = data.xpath('//*[@id="tdata"]/tr[' + str(i) + ']/td[12]/text()')[0]
    print(second_prize_size, end='\t')
    second_prize = data.xpath('//*[@id="tdata"]/tr[' + str(i) + ']/td[13]/text()')[0]
    print(second_prize, end='\t')
    total_bet_amount = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[14]/text()')[0]
    print(total_bet_amount, end='\t')
    result_day = data.xpath('//*[@id="tdata"]/tr['+str(i)+']/td[15]/text()')[0]
    print(result_day, end='\t')


    print(i) 

    pos ={
        'result_num': result_num,
        'resrult_bef1': resrult_bef1,
        'resrult_bef2': resrult_bef2,
        'resrult_bef3': resrult_bef3,
        'resrult_bef4': resrult_bef4,
        'resrult_bef5': resrult_bef5,
        'resrult_beh1': resrult_beh1,
        'resrult_beh2': resrult_beh2,
        'prize_pool': prize_pool,
        'first_prize_size': first_prize_size,
        'first_prize': first_prize,
        'second_prize_size': second_prize_size,
        'second_prize': second_prize,
        'total_bet_amount': total_bet_amount,
        'result_day': result_day,
    }
    requests.append(pos)
    # print(requests)

df = pd.DataFrame(requests)
df.to_csv('/Users/lianxiaobao/lianxiaobao/bigdatabook/daletou.csv', mode='a')
