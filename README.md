# bsn_app_explorer
BSN-APP 业务浏览器

本文件用于对运行Python开发示例进行相关描述：

 一、开发环境准备 
 
1、Pycharm（可以使用您习惯的IDE）  
2、SQLAlchemy==1.3.10<br>
3、Flask==1.1.1<br>
4、bsn_sdk==0.1.3<br>
5、Flask_SQLAlchemy==2.4.1<br>
6、sqlalchemy_migrate==0.13.0<br>
7、configparser==4.0.2 

（注：可根据requirements.txt文件自动安装依赖 执行命令 pip install -r C:\Users\Administrator\requirements.txt）

二、项目描述

该项目使用flask框架，直接调用服务网关api接口，实现数据交互。

结构说明：		
1、docs api说明文档

2、certificate 文件夹下文件说明：bsn_https.pem（https请求的公钥证书）<br>
			 gateway_public_cert.pem（网关公钥证书）<br>
			 private_key.pem（用户私钥证书）<br>
			 public_cert.pem（用户公钥证书）

3、logs 文件夹下存放日志文件。

三、代码运行

安装好开发环境后，进入项目根目录下，cmd下运行 python manage.py runserver 运行项目。<br>
在浏览器中输入 http://127.0.0.1:5000/ 即可访问项目的web界面。


