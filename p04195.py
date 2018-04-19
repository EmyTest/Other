from urllib import  request,parse
import json
baseurl = 'http://fanyi.baidu.com/sug'
#存放用来模拟form的数据一定是dict格式
data = {
    #girl 是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
    'kw':'girl'
}
#需要用parse模块进行编码
data = parse.urlencode(data).encode("utf-8")
#构造一个请求头，请求头至少包括传入的数据长度
#request要求传入的请求头是一个dict格式
headers ={
    #因为使用post请求，至少应该包含content-length 字段
    'Content-Length':len(data)

}
#构造一个request的实例
req = request.Request(url=baseurl,data=data,headers=headers)
#因为已经构造了一个request的请求实例，则所有的请求信息都可以封装在request实例里面
#有了headers，data，url 就可以尝试发出请求了
rsp = request.urlopen(req)
json_data = rsp.read().decode()
print(json_data)
#把json字符串转化为字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)
