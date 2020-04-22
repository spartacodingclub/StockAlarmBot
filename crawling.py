import requests
from bs4 import BeautifulSoup as bs


def crawl(stock_name):
    url="https://www.google.com/search?q="
    url=url+stock_name+"+stock"
    response=requests.get(url)


    if response.status_code != 200:
        # print("hi")
        return "request failed"
    else:
        pass

    source=response.text
    soup=bs(source,'html.parser')
    select_stock_name=soup.select('span[class="r0bn4c rQMQod"]')

    if not select_stock_name:
        return "List is empty"
    else:
        pass

    exist=0
    stock=""
    for i in select_stock_name:
        for item in i:
            if stock_name.upper() == item[:-8]:
                exist=1
                stock=item
            elif stock_name.upper() == item[:-10]:
                exist=1
                stock=item
    if exist == 0:
        return "that stock not exists"
    # 여기까지가 주식 이름 뽑기


    select_stock_value = soup.select('div[class="BNeawe iBp4i AP7Wnd"]')
    i=0
    value=0
    per=0
    for item in select_stock_value[1]:
        if i == 0:
            value=item
        if i == 1:
            per = str(item)[28:-7]
            per=per.replace(" ","")
        i=i+1

    return stock+" "+ value + per



# crawl_index 구현중...
def crawl_index():
    url ="https://kr.investing.com/indices/major-indices"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        # print("hi")
        return "request failed"
    else:
        pass

    index_list=list()

    source = response.text
    soup = bs(source, 'html.parser')
    indexes = soup.select('.genTbl closedTbl elpTbl elp20 crossRatesTbl > tbody > tr')

    for index in indexes:
        index_name=index.select_one('.bold left plusIconTd noWrap elp > a[title]')
        if index_name =="나스닥종합지수"


    # text=open('./new.html', 'w',-1,"utf-8")
    # text.write(source)
    # text.close()

    return source

