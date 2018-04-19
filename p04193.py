import urllib
from urllib import request,parse


if __name__=='__main__':
    url = "https://www.baidu.com/s?"
    wd = input("input your keyword: ")
    #想要使用data，需要使用字典结构
    qs ={
        "wd":wd
    }
    #转换url编码
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = urllib.request.urlopen(url)
    html = rsp.read()

    html = rsp.read()

    html = html.decode()
    print(html)

    html = rsp.read()