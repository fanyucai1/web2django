# 快速开始

1.  安装django并创建新的project
```{.cs}
pip3 install Django
django-admin startproject myproject
cd myproject
mkdir -p templates/admin
mkdir -p static/
mkdir -p media/
```

2.  安装simpleui，并且下载simpleui的demo作为参考学习链接
```{.cs}
pip3 install django-simpleui
wget https://github.com/newpanjing/simpleui_demo/archive/refs/heads/master.zip
unzip master.zip
rm -rf master.zip
```

3.  修改myproject/settings.py
```{.cs}
import os #添加
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
ALLOWED_HOSTS = ['*']#允许访问所有host
LANGUAGE_CODE = 'zh-hans'#支持中文修改
TIME_ZONE = 'Asia/Shanghai'#支持中文修改
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")#添加
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')#添加
MEDIA_URL = 'media/'#添加

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#添加本地模版文件
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

4.  创建管理员账号，将simpleui静态文件静态文件克隆到根目录
```{.cs}
python3 manage.py collectstatic
```

5.  修改myproject/urls.py
```{.cs}
urlpatterns = [
    path('', admin.site.urls),#添加项
]
```

6.  启动服务器，IP地址和端口可改
```{.cs}
python3 manage.py runserver 127.0.0.1:8000
```

7-1. 创建app
```{.cs}
python3 manage.py startapp myapp
cd myapp/
创建urls.py脚本
cd myapp/
mkdir templates/
```

7-2.    给你的app改个名字,修改myapp/apps.py脚本
```{.cs}
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    verbose_name="宏基因组数据分析"#添加行，verbose_name的意思，就是给你的模型类起一个更可读的名字
```

7-3. 修改myapp/models.py脚本，定义新的数据表格
```{.cs}
def user_directory_path(instance, filename):#为了实现上传的文件动态存储
    return 'user_data/{0}/{1}'.format(instance.project, filename)

class task(models.Model):
    project= models.CharField(max_length=100, verbose_name='项目编号')
    pub_date=models.DateTimeField(auto_now_add=True,verbose_name="上传时间")
    fastq_R1= models.FileField(upload_to=user_directory_path,verbose_name="R1 fastq")
    fastq_R2= models.FileField(upload_to=user_directory_path,verbose_name="R2 fastq")
    class Meta:
        verbose_name = "数据分析"
        verbose_name_plural = "数据分析"
```
数据类型
```{.cs}
no = models.AutoField(primary_key=True, verbose_name='编号')#自增ID字段，默认会生成一个名称为id的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True
name = models.CharField(max_length=50, verbose_name='名称')#用于较短的字符串，如要保存大量文本, 使用TextField。必须max_length参数
is_hot = models.BooleanField(verbose_name='是否热门')#存储True或False
file_upload = models.FileField(upload_to="uploads/%Y/%m/%d/")#file will be saved to MEDIA_ROOT/uploads/2015/01/30
photo_upload= models.ImageField(upload_to="uploads/%Y/%m/%d/",verbose_name='照片')#继承FileField 的所有属性和方法，但也验证上传的对象是有效的图像
```
7-4. 注册模型类,修改myapp/admin.py，添加以下内容
```{.cs}
from .models import task #添加
class taskModelAdmin(admin.ModelAdmin):
    list_display = ('project','pub_date','fastq_R1','fastq_R2')

admin.site.register(task,taskModelAdmin)
```

# FAQ:

1.  Django 运行端口被占用 Error: That port is already in use
```{.cs}
lsof -i:8000
```

2. django.db.utils.OperationalError: no such table: django_sessio
```{.cs}
python3 manage.py migrate
```

3.开发过程中app数据更新
```{.cs}
删除：myapp/migrations/下除__init__.py所有文件
删除：db.sqlite3
python3 manage.py makemigrations myapp
python3 manage.py migrate
python3 manage.py createsuperuser
```


/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages