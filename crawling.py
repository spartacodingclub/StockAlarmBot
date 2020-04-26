import requests
import json
from bs4 import BeautifulSoup as bs


def crawl(stock_name):
    url="https://www.google.com/search?q="
    url=url+stock_name+"+stock"
    response=requests.get(url)


    if response.status_code != 200:
        # print("hi")
        return "request failed"


    source=response.text
    soup=bs(source,'html.parser')
    select_stock_name=soup.select('span[class="r0bn4c rQMQod"]')

    if not select_stock_name:
        return "List is empty"

    exist=False
    stock=""
    for i in select_stock_name:
        for item in i:
            if stock_name.upper() == item[:-8]:
                exist=True
                stock=item
            elif stock_name.upper() == item[:-10]:
                exist=True
                stock=item
    if exist == False:
        return "that stock not exists"
    # 여기까지가 주식 이름 뽑기


    select_stock_value = soup.select('div[class="BNeawe iBp4i AP7Wnd"]')
    i=0
    value=0
    per=0
    # value = select_stock_value[1][0]
    # item = select_stock_value[1][1]
    # per = str(item)[28:-7]
    # per = per.replace(" ", "")

    for item in select_stock_value[1]:
        if i == 0:
            value=item
        if i == 1:
            per = str(item)[28:-7]
            per=per.replace(" ","")
        i=i+1

    result= stock+" "+value+per

    return result



# crawl_indices 구현중...
def crawl_indices():
    url ="https://kr.investing.com/indices/major-indices"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        # print("hi")
        return "request failed"

    source = response.text
    soup = bs(source, 'html.parser')
    indices_soup = soup.select('table.genTbl.closedTbl.elpTbl.elp20.crossRatesTbl > tbody > tr')
    # table[class='genTbl closedTbl elpTbl elp20 crossRatesTbl']

    indices_list=crawl_indices_nasdaq(indices_soup)
    indices_list+=crawl_indices_dow(indices_soup)
    indices_list+=crawl_indices_snp500(indices_soup)
    indices_list+=crawl_indices_kospi(indices_soup)
    indices_list+=crawl_indices_kosdaq(indices_soup)
    print(indices_list)

    return indices_list


def crawl_indices_nasdaq(indices_soup):
    # indices_dict=dict(nasdaq="")
    indices_str=""
    for indice in indices_soup:
        if indice.select_one('.bold.left.plusIconTd.noWrap.elp > a[title="나스닥종합지수"]'):
            # indices_dict["nasdaq"]=list()
            indices_str+="NASDAQ"
            indices_str+=" "

            value=str(indice.select_one(".pid-14958-last"))[27:-5]
            # value=dict(value=value)
            # indices_dict["nasdaq"].append(value)
            indices_str+=value
            indices_str+=" "

            change=str(indice.select_one(".bold.greenFont.pid-14958-pc"))[40:-5]
            # change=dict(change=change)
            # indices_dict["nasdaq"].append(change)
            indices_str+=change
            indices_str+=" "

            change_per=str(indice.select_one(".bold.greenFont.pid-14958-pcp"))[41:-5]
            # change_per=dict(change_per=change_per)
            # indices_dict["nasdaq"].append(change_per)
            indices_str+=change_per
            indices_str+=" "

    return indices_str

def crawl_indices_dow(indices_soup):
    # indices_dict=dict(dow="")
    indices_str=""
    for indice in indices_soup:
        if indice.select_one('.bold.left.plusIconTd.noWrap.elp > a[title="다우존스"]'):
            # indices_dict["dow"]=list()
            indices_str+="DowJones"
            indices_str+=" "

            value=str(indice.select_one(".pid-169-last"))[26:-5]
            # value=dict(value=value)
            # indices_dict["dow"].append(value)
            indices_str+=value
            indices_str+=" "


            change=str(indice.select_one(".bold.greenFont.pid-169-pc"))[38:-5]
            # change=dict(change=change)
            # indices_dict["dow"].append(change)
            indices_str+=change
            indices_str+=" "

            change_per=str(indice.select_one(".bold.greenFont.pid-169-pcp"))[39:-5]
            # change_per=dict(change_per=change_per)
            # indices_dict["dow"].append(change_per)
            indices_str+=change_per
            indices_str+=" "

    return indices_str

def crawl_indices_snp500(indices_soup):
    # indices_dict=dict(snp500="")
    indices_str=""
    for indice in indices_soup:
        if indice.select_one('.bold.left.plusIconTd.noWrap.elp > a[title="S&P 500"]'):
            # indices_dict["snp500"]=list()
            indices_str+="S&P500"
            indices_str+=" "

            value=str(indice.select_one(".pid-166-last"))[25:-5]
            # value=dict(value=value)
            # indices_dict["snp500"].append(value)
            indices_str+=value
            indices_str+=" "

            change=str(indice.select_one(".bold.greenFont.pid-166-pc"))[38:-5]
            # change=dict(change=change)
            # indices_dict["snp500"].append(change)
            indices_str+=change
            indices_str+=" "

            change_per=str(indice.select_one(".bold.greenFont.pid-166-pcp"))[39:-5]
            # change_per=dict(change_per=change_per)
            # indices_dict["snp500"].append(change_per)
            indices_str+=change_per
            indices_str+=" "

    return indices_str

def crawl_indices_kospi(indices_soup):
    # indices_dict=dict(kospi="")
    indices_str=""
    for indice in indices_soup:
        if indice.select_one('.bold.left.plusIconTd.noWrap.elp > a[title="코스피지수"]'):
            # indices_dict["kospi"]=list()
            indices_str+="KOSPI"
            indices_str+=" "

            value=str(indice.select_one(".pid-37426-last"))[27:-5]
            # value=dict(value=value)
            # indices_dict["kospi"].append(value)
            indices_str+=value
            indices_str+=" "

            change=str(indice.select_one(".bold.redFont.pid-37426-pc"))[38:-5]
            # change=dict(change=change)
            # indices_dict["kospi"].append(change)
            indices_str+=change
            indices_str+=" "

            change_per=str(indice.select_one(".bold.redFont.pid-37426-pcp"))[39:-5]
            # change_per=dict(change_per=change_per)
            # indices_dict["kospi"].append(change_per)
            indices_str+=change_per
            indices_str+=" "

    return indices_str

def crawl_indices_kosdaq(indices_soup):
    # indices_dict=dict(kosdaq="")
    indices_str=""
    for indice in indices_soup:
        if indice.select_one('.bold.left.plusIconTd.noWrap.elp > a[title="코스닥"]'):
            # indices_dict["kosdaq"]=list()
            indices_str+="KOSDAQ"
            indices_str+=" "

            value=str(indice.select_one(".pid-38016-last"))[27:-5]
            # value=dict(value=value)
            # indices_dict["kosdaq"].append(value)
            indices_str+=value
            indices_str+=" "

            change=str(indice.select_one(".bold.redFont.pid-38016-pc"))[38:-5]
            # change=dict(change=change)
            # indices_dict["kosdaq"].append(change)
            indices_str+=change
            indices_str+=" "

            change_per=str(indice.select_one(".bold.redFont.pid-38016-pcp"))[39:-5]
            # change_per=dict(change_per=change_per)
            # indices_dict["kosdaq"].append(change_per)
            indices_str+=change_per
            indices_str+=" "

    return indices_str



def crawl_future_indices():
    pass


crawl_indices()