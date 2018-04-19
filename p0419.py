from urllib import request
import urllib
import chardet
#
# import requests
if __name__=='__main__':
    url = "http://jobs.zhaopin.com/CZ198295010J00046605906.htm?ssidkey=y&ss=201&ff=03&sg=96016aaf5059471ba92cb2ed2c2a7bc8&so=5"
    rsp=urllib.request.urlopen(url)
    #把返回的结果读取出来
    #读取出来的内容类型为bytes
    html = rsp.read()
    #用dectect自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    #如果把bytes内容转换为字符串，需要解码
    #使用get取值保证不会错
    html=html.decode(cs.get("encoding","utf-8"))
    print(html)


