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

