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