http 协议请求响应模型
场景：登录
1、客户端发起请求到api接口层
   1.1 用户在客户端填写用户名。密码，点击登录，发送请求
   2.1api对业务逻辑进行验证
      2.1.1 验证用户名和密码是否合法
  
3、api会将用户输入的数据发给db层
create read  update  delete

select * from user where 

3.1 数据库查询成功则返回1 失败返回0

4、db会将返回值的查询数据库的条目数给api
5、api返回成功或失败的状态码给客户端
6、客户端将返回信息提示给用户

一、客户端
    功能测试、性能、自动化
二、接口层
    接口测试，功能测试，性能测试、自动化
三、数据库层
    
    http://127.0.0.1:8080?username=zhangsan&password=123
    http://127.0.0.1:8080
    请求体
    [
        [
        username
            ]
    
    ]
 
 PUT:向指定资源位置上传其最新内容
 
 jmeter
 BS架构应用性能
 HTTP协议接口功能和性能
 FTP 上传下载文件
 
 Mysql数据库性能
 mangodb数据库性能
 支持自定义java组开发
 
 
 
 
 
 #######
【乱码】
 后置处理器 - BeanSjell PostProcessor
 prev.setDataEncoding("utf-8")
 
 
 【【正则表达式】】
 match tracer
 
 http://tool.oschina.net/regex/
 
 .    匹配除了换行符之外的任何字符
 \w   匹配字母或数字或下划线或汉字
 \s   匹配任意空白符
 \d   匹配数字
 \b   匹配单词的开始或结
 ^    匹配字符串的开始
 $    匹配字符串的结束
 
 *    重复零次或多次
 +    重复一次或多次
 ？   重复零次或一次
 {n}  重复n次
 {n,} 重复n次或多次
 {n，m} 重复n次到m次
 
 
 添加线程组
 添加Http信息头管理器：将参数化的信息头部分的参数记录在管理器中
 添加http请求默认值：填写【服务器名称或ip】   parameters是否有必要填写？
 创建http请求 ：
 1、登录http： 服务器名称或ip  /  路径eg：/w***r_u**s_a**/v1/s*****/****te
     【正则表达式提取器】
     1.1提取信息头里面的参数：“要检测的响应字段”：信息头；引用名称：A-Token-Header  正则表达式：A-Token-Header: (.+)  【出错点】 冒号后面有空格；不要参数前后的引号
     1.2提取响应数据里面的参数：“要检测的响应字段”：主体 ；。。。。。其他要注意的：比如：模板  $1$等
2、接口二：
      注意传参 ${**}
      
3、运行情况见百度云（131）

4、参数化设置：
   将“创建oac系列”这个接口循环两次，传入不同的参数：
   - 创建循环控制器 ：2次循环
   - 创建CSV Data Set Config： 
   
   Allow quoted data？：是否允许引用数据。默认设置为 false。例如数据样式为："101-005-98536","29357","1","1993575","477948510289","android","45" 时，此处需设置为 true，一般默认为 false 即可。
   Recycle on EOF?：是否循环读取参数文件内容。默认设置为 true。设置为 true 时，当已经读取完参数文件内的测试用例数据，还需要继续获取用例数据时，此时会循环读取参数文件数据；设置为 false 时，若已至文件末尾，则不再继续读取测试数据。通常在 线程组的线程数 * 线程组的循环次数 > 参数文件行数时，才需要将此项设置为 true。
   Sotp thread on EOF?：当读取到参数文件末尾时，是否停止读取线程。默认为 false。当 Recycle on EOF?  设置为 true 时，此项不起任何作用。当且仅当 Recycle on EOF? 为 false 时，此项配置才生效。
                        若为 true，则在读取到参数文件行末尾时，终止参数文件读取线程。例如：线程组的线程数 * 线程组的循环次数 = 10，参数文件行数 = 7，那么将在第 8 次开始停止线程。
                        若为 false，此时线程会继续读取，但是会请求错误，因此时读取的数据为 EOF。以上同例，自第 8 次开始，线程的请求数据为 EOF。
   
 
 filename：可以写相对路径 【相对路径怎么描述】
 
 
 响应断言 执行结果：

   -如果接口响应数据可以与断言匹配上，则测试用例通过，否则不通过。可以通过断言结果，查看断言执行情况。
   
   
 ##BeanShell断言：
 String data = SampleResult.getResponseDataAsString();
if (data.indexOf("\"success\":true") != -1 || data.indexOf("\"Code\":200") != -1) {
    SampleResult.setSuccessful(true); 
}
else {
    SampleResult.setSuccessful(false); 
}




0417：
根据部分业务
关于注册获取验证码的坑：
1、按照教程来设置JDBC Connection Configuration 时： 写数据库url 多加了一个空格 导致花费了大量时间修改
2、随机邮箱生成，可以用 randonstring 来做参数化   注意邮箱的写法 后面直接+ @qq.com 等等
3、部分接口的调试： 报错 可能是因为 上一个接口的返回值有调整，导致 设置参数的时候 ，正则表达式需要跟着变化
4、get、post等请求  不要弄错
5、注意JDBC Request  值的获取  如 查询： select message from t_message_log where phone= '${target}' order by updated_at desc limit 1



jmeter    问题描述：我的一系列接口测试里面 涉及到多个账号登录的问题  就需要用到头部的登录token    比如 1、a账号登录   2、a账号发单    3、b账号也登录  4、b账号用步骤3的登录token 和其他的参数 传值       接单    此时我的线程组 http信息头管理器里面是a的token   b的token不知道怎么传  是设两个线程组（似乎一个线程组只能有一个头部管理器的token）   然后跨线程组   取其他的参数     还是    就用一个线程组  把第二个账号的token参数化    参数化传值的话   和其他参数一起传在body里面  好像不对


中间的解决方法：
（线程组一）
1、a登录
2、a发单 ：添加正则表达式提取器获取orderid（线程组2里面会用到）-->  添加 beanshellpostprocessor 【填写 parameters ：${orderId}      script：String orderid=bsh.args[0];
print (orderId)
${__setProperty(orderIdNew,${orderId},true)}   】

线程组二：
3、b登录
4、b接单 b的传参  （a里面的参数：targetId   ： ${__property(orderIdNew,,true)}）

注意：
勾选【测试计划】里面 “独立运行每个线程组”
或：
第一个线程组用  ：setup thread group

待解决疑问点：setup thread group   和  线程组的详细不同点

之后51test给出的解决参考：https://c.m.163.com/news/a/DEFA4S5K0511G03U.html?spss=newsapp&spsw=1
【BeanShellPreProcessor】和 beanshellpostprocessor的不同点：

![图一][http//wx2.sinaimg.cn/thumb150/b278a87fgy1fqhqr4tgecj20u80e0taf.jpg]

![图二][http//wx4.sinaimg.cn/thumb150/b278a87fgy1fqhqr4j1mwj20rz0edgly.jpg]

