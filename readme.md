#安装
pyhton3.7  
nginx  
mysql  
#步骤
sudo yum install mysql-devel
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
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