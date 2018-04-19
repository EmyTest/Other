from urllib import request,error
if __name__ == '__main__':
    # url ='http://www.baidu.com/welcome.html'
    url = "http://www.sipo.gov.cn/www"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
    except error.URLError as  e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))

    except Exception as e:
        print(e)

'''
HTTPError是URLError的一个子类
HTTPError和URLError的区别：
HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发HTTPError
URLError对应的一般是网络出现问题，包括URL问题
OSError  -- URLError -- HTTPError

'''