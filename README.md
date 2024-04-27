# 快速开始

1.  安装django并创建新的project
```{.cs}
pip3 install Django
django-admin startproject myproject #创建新的project,名字可改
cd myproject
mkdir -p templates/admin
mkdir -p static/
mkdir -p media/
python3 manage.py collectstatic #默认把django对应的静态文件，拷贝到当前项目目录下，也就是static/目录下
python3 manage.py startapp myapp #创建app,名字可改
cd myapp/
#可创建urls.py脚本，以后这个app对应的url可以都写在这个里面，如果项目较小也可以不写(非必须)
mkdir templates/ #同样针对这个app的html模版也可以放在这个文件夹里(非必须)
```

2.修改myproject/settings.py
```{.cs}
import os #添加
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',#添加以后创建新的app就把名字写在这里，这个名字是myapp/apps.py模块名字
]
ALLOWED_HOSTS = ['*']#允许访问所有host
LANGUAGE_CODE = 'zh-hans'#支持中文修改
TIME_ZONE = 'Asia/Shanghai'#支持中文修改
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")#添加 （你的静态文件存放目录，例如你程序需要加载的图片以及css文件等）
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')#添加 （用户上传的文件默认会上传到这个路径下）
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

3.  修改myproject/urls.py
```{.cs}
urlpatterns = [
    path('', admin.site.urls),#修改项,这样在启动第4步的时候，就是登陆页面了，否则默认是http://127.0.0.1:8000/admin
]
```

4.创建超级用户
```{.cs}
python3 manage.py createsuperuser #提示输入邮箱可以回车直接忽略
```

5.  启动服务器，IP地址和端口可改,在浏览器输入对应的IP地址，然后输入刚才的用户名以及密码就可以实现登陆
```{.cs}
python3 manage.py runserver 127.0.0.1:8000
```
登陆的django模版实际位于你安装的django目录(如下)的index.html
```{.cs}
/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/django/contrib/admin/templates/index.html
```
你可以将该index.html拷贝到刚才创建的templates/admin目录下进行修改，或者你自己编写一个html文件，但是名字必须是index.html

6.  登陆后页面上显示的有你app的名字如果想改个名字,请修改myapp/apps.py脚本
```{.cs}
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    verbose_name="宏基因组数据分析"#添加行，verbose_name的意思，就是给你的模型类起一个更可读的名字
```

7. 接下来就是定义数据表格也就是models,修改myapp/models.py脚本，定义新的数据表格主要是以class开头
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
表格对应的数据类型有很多，常用的有如下：
```{.cs}
no = models.AutoField(primary_key=True, verbose_name='编号')#自增ID字段，默认会生成一个名称为id的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True
name = models.CharField(max_length=50, verbose_name='名称')#用于较短的字符串，如要保存大量文本, 使用TextField。必须max_length参数
is_hot = models.BooleanField(verbose_name='是否热门')#存储True或False
file_upload = models.FileField(upload_to="uploads/%Y/%m/%d/")#file will be saved to MEDIA_ROOT/uploads/2015/01/30
photo_upload= models.ImageField(upload_to="uploads/%Y/%m/%d/",verbose_name='照片')#继承FileField 的所有属性和方法，但也验证上传的对象是有效的图像
```

8. 定义完了数据表，然后注册模型类,修改myapp/admin.py，添加以下内容
```{.cs}
from .models import task #添加
class taskModelAdmin(admin.ModelAdmin):
    list_display = ('project','pub_date','fastq_R1','fastq_R2')#list_display就是要展示那些条目

admin.site.register(task,taskModelAdmin)
```

9.我在这里创建了2个models,一个models是用来客户上传数据并启动后台数据分析task，一个models是展示数据分析结果result，另外我想实现两个models
实现对task增删也会同步显示result,所以我添加了signals.py脚本，该脚本会对客户上传的数据进行同步删除，客户只能编辑task,不能编辑result页面

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
rm -rf db.sqlite3
python3 manage.py makemigrations myapp
python3 manage.py migrate
python3 manage.py createsuperuser
```

# linux部署:Django+uwsgi+nginx

Nginx负责接收和处理客户端的HTTP请求，并提供静态文件服务、负载均衡和缓存等功能，而uWSGI负责运行Django应用程序，并处理与之相关的通信和请求。它们的配合使得Django应用程序能够高效、稳定地提供Web服务。

1. uwsgi是python模块
```{.cs}
pip3 install uwsgi
uwsgi --ini /path/to/uwsgi.ini
```

2. 安装nginx
```{.cs}
yum install nginx
systemctl start nginx.service#启动nginx服务
systemctl enable nginx#Linux开机默认启动nginx服务
```
