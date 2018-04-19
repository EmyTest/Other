import urllib
from urllib import request


if __name__=='__main__':
    url = "http://jobs.zhaopin.com/CZ198295010J00046605906.htm?ssidkey=y&ss=201&ff=03&sg=96016aaf5059471ba92cb2ed2c2a7bc8&so=5"
    rsp=urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.geturl()))

    html = rsp.read()

    html=html.decode()
    print(html)
