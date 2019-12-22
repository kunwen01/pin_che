#安装
pyhton3.7  
nginx  
mysql  
#步骤
sudo yum install mysql-devel
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  

