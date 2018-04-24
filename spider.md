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

handler 是handler的实例，常用参考代码实例  
-用来处理复杂请求
  #生成cookie管理器        
  cookie_handler = request.HTTPCookieProcessor(cookie)          
  #创建http请求管理器             
  http_handler = request.HTTPHandler()          
  #生成http管理器         
  https_handler = request.HTTPHandler()      
  
  
  创建handler后，使用openler打开，打开后相应的业务由相应的handler处理   
  cookie作为一个变量，打印出来  
      -cookie的属性：  
        -name：名称  
        -value：值  
        -domain：可以访问此cookie的域名          
        -path ：可以访问此cookie的页面路径      
        -expires：过期时间       
        -size：大小          
        -http字段：   
  
  cookie的保存：FileCookieJar
       

SSL   
  -SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书{SercureSocketLayer}  
  -美国网景公司开发  
  -CA（ certificateauthority）数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构   
 
