1.  安装django
```{.cs}
pip3 install Django
```
2.  创建project ::
```{.cs}
django-admin startproject myproject
```
3.  创建app
```{.cs}
cd myproject/
django-admin startapp myapp
```
4.  创建文件夹,存放渲染文件
```{.cs}
mkdir -p static/css/
mkdir -p static/js/
mkdir -p static/vendor/
mkdir -p templates/
mkdir -p upload/
```
5.  修改myproject/settings.py
```{.cs}
ALLOWED_HOSTS = ["*"]#修改添加*号,这样就可以使用localhost使用了
INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            **'myapp',**#添加的部分为上面建立的app的名字
        ]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#修改部分
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

LANGUAGE_CODE = 'zh-hans' #修改
TIME_ZONE = 'Asia/Shanghai' #修改
USE_I18N = True
USE_L10N = True
USE_TZ = False #修改

STATIC_URL = '/static/'
#添加如下：
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

#事实上MEDIA_ROOT和MEDIA_URL代表的是用户上传后的文件一般保存的地方,在Django的FileField和ImageField这样的Model类中，
有upload_to参数可选。#当upload_to设置相关的地址后，如：upload_to="username"；
文件上传后将自动保存到 os.path.join(MEDIA_ROOT, upload_to)。所以可以添加如下代码

MEDIA_ROOT=os.path.join(BASE_DIR,'upload')
```

6.  启动服务器
```{.cs}
python3 manage.py runserver 8080
# 默认localhost=127.0.0.1,浏览器访问 http://127.0.0.1:8080 or  http://localhost:8080
# 也可以更改IP地址
python manage.py runserver 0.0.0.0:8000
```


