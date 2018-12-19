"""


"""
import random
import time
import os
import re
from lxml import etree

import requests

# 基础url
BASEURL = 'http://www.jyeoo.com/chinese/ques/partialques?f=0&q=bb552884-64a5-47fd-b70a-d307f4731084~cc998ecf-bf57-430e-8e64-bbd215756604~&lbs=&pd=1&pi=undefined&r=0.7368134808426823'

userAgent_list = [
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
]



# 解析网页源代码
def pasePage(data,perStr):
    per = re.compile(perStr)
    reuslt_list = per.findall(data)
    return reuslt_list


# 通过xpath解析网页源代码
def pasePageByXpath(html,xpathStr):
    """
    :param html:      需要解析的的html 文本
    :param xpathStr:  xpath规则字符串
    :return:          返回匹配到的字符串
    """
    # 创建解析对象
    parseHtml = etree.HTML(html)
    r_list = parseHtml.xpath(xpathStr)
    return r_list




# 获取网页的源代码
def getPage(url):
    global userAgent_list
    userAgent = random.choice(userAgent_list)
    headers = {
        "User-Agent":userAgent
    }

    response = requests.get(url=url,headers = headers)
    return response.text


# 写入本地文件
def writeToLocalhostFile(filename,data):
    with open(filename,'a',encoding='utf-8') as f:
        f.write(data)
    return


# 点击下一页
def clickNextPage():
    pass


def main():
    html = getPage(url=BASEURL)
    li_list = pasePageByXpath(html,"/html/body/div/ul/li")
    print(len(li_list))
    quesList = []
    for li in li_list:
        # 问题标题
        quesTitle = li.xpath(".//fieldset/div[@class='pt1']/text()")[0].strip()
        a = li.xpath(".//fieldset/div[@class='pt2']")
        if not a:
            b = li.xpath(".//fieldset/div[@class='pt1']/div/text()")
            print(b)
        if a:
            c = a[0].xpath(".//table/tr")
            for d in c:
                e = d.xpath(".//td")[0]
                print(e)




    # if li_list:
    #     li = li_list[len(li_list)-1]
    #     print(li)
    #     ques = pasePage(li,quesStr)
    #     centent = pasePage(li,cententStr)
    #     if not centent:
    #         cententStr = r'<div class="quizPutTag">(.*?)</div>|<div class="sanwser">(.*?)</div>'
    #         centent = pasePage(li, cententStr)
    #         centent_ = []
    #         for one,two in centent:
    #             if one:
    #                 centent_.append(one)
    #             if two:
    #                 centent_.append(two)
    #         print(centent_)

if __name__ == '__main__':
    main()





