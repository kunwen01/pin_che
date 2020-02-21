#安装
pyhton3.7  
nginx  
mysql  
#步骤
sudo yum install mysql-devel
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
#### 启动：
uwsgi --ini xxx.ini
#### 重启：
uwsgi --reload xxx.pid
#### 停止：
uwsgi --stop xxx.pid
#### setting修改  
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#### urls修改
from django.conf.urls.static import static  
from django.conf import settings  
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#### 静态文件处理
python manage.py collectstatic

#### 启动定时任务
将任务添加并生效  
python manage.py crontab add  
显示当前的定时任务  
python manage.py crontab show  
删除所有定时任务  
python manage.py crontab remove  
重启django服务  
执行定时任务  
corntab -e

#### app
  1、临时下载地址，只能下载5次  
    Android 公共测试证书 [下载地址]( https://service.dcloud.net.cn/build/download/bba7b740-2c85-11ea-9738-ed494c7f20d3)  
    iOS越狱包 [下载地址](https://service.dcloud.net.cn/build/download/bb95fb50-2c85-11ea-b402-9767c6c3c940)  
    Android 公共测试证书 [下载地址](https://service.dcloud.net.cn/build/download/744f6320-2c97-11ea-adbe-1bfdc0c117b1) 
    
#### 同步到数据库增加字段（或新表）
python manage.py makemigrations AppTest  
        Select an option: exit  
        Please select a valid option: 2  
python manage.py migrate  
（python manage.py syncdb）
