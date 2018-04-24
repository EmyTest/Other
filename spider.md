cookies和session的区别：  
存放的位置不同   
cookies 不安全  
session会保存在服务器上一定时间。会过期  
单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个  

session的存放位置   
存放在服务器端        
一般情况 session是放在内存或数据库中         
没有cookies登录 案例sp424.py可以看到 ，如果没有使用cookies则反馈网页为未登录状态

使用cookie登录：  
直接把cookie复制下来，然后手动放入请求头        

http模块包含一些关于cookie的模块，通过它们我们可以自动使用cookie           

  1、CookieJar   
         管理存储cookie，向传出的http请求添加cookie           
         cookie存储在内存中，cookie实例收后cookie将消失          
  2、 FileCookieJar  （filename，delayload=None,policy=None）        
         使用文件管理cookie           
         filename是保存cookie的文件      
  3、MozillaCookieJar     
         创建与Mozilla浏览器cookie，txt兼容的FileCookieJar实例         
  4、LwpCookieJar   （filename，delayload=None,policy=None）：    
         创建与libwww-per标准兼容的set-cookie3格式的filecookiejar实例        
  他们的关系 ： 1-->2-->3-->4   
  
  
  利用cookiejar访问人人，案例13   
  流程：  
    打开登录页，用户名密码登录   
    自动提取的cookie  
    利用提取的cookie登录隐私页面  
