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

7. 创建app
```{.cs}
python3 manage.py startapp myapp
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