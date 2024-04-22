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
    'simpleui', #添加的部分为上面建立的app的名字
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
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]#添加本地静态文件目录

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
######以下是针对simpleui的参数修改设定
SIMPLEUI_STATIC_OFFLINE = True#指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
SIMPLEUI_HOME_ACTION = False#取消主页面显示最近动作
SIMPLEUI_HOME_INFO = False#不显示服务器信息
```

4.  创建管理员账号，将simpleui静态文件静态文件克隆到根目录
```{.cs}
python3 manage.py migrate
python3 manage.py createsuperuser
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
class task(models.Model):
    pub_date=models.DateTimeField(verbose_name="时间")
    user_test=models.CharField(verbose_name="用户名",max_length=200)
    class Meta: #可有可无
        table_name='my_owner_table'#重新定义数据表格的名称
        managed = False #默认为TRUE,可以对数据库表进行migrate或migrations、删除等操作
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
    list_display = ('pub_date','user_test')
    search_fields = ('user_test',)
    ordering = ('user_test',)
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



/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages