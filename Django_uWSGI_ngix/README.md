# 1.参考链接：

[Setting up Django and your web server with uWSGI and nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

[Django Nginx+uwsgi 安装配置](https://www.runoob.com/django/django-nginx-uwsgi.html)

[如何用 uWSGI 托管 Django](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/wsgi/uwsgi/#)

# 2.uWSGI负责运行Django应用程序，并处理与之相关的通信和请求。它们的配合使得Django应用程序能够高效、稳定地提供Web服务
```{.cs}
pip3 install uwsgi
uwsgi --ini /path/to/uwsgi.ini
```
uwsgi.ini示例：
```{.cs}
[uwsgi]
chdir=/staging4/fanyucai/web2django/myproject/
module=myproject.wsgi
master=True
socket=10.88.32.72:9003
vacuum = true
buffer-size=65536
```

# 3. nginx负责接收和处理客户端的HTTP请求，并提供静态文件服务、负载均衡和缓存等功能
```{.cs}
yum install nginx
systemctl start nginx.service#启动nginx服务
systemctl enable nginx#Linux开机默认启动nginx服务
```
新建uwsgi_params文件，内容如下：
```{.cs}

uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
```

# 4.在不改变原/etc/nginx/nginx.conf配置的情况建议在你的项目下新建mysite_ngix.conf,内容如下：
```{.cs}
upstream django {
    server 10.88.32.72:9001;
}

server {
    listen      9002;
    server_name example.com;
    charset     utf-8;

    client_max_body_size 75M;   # adjust to taste

    location /media  {
        alias /staging4/fanyucai/web2django/myproject/media;
    }

    location /static {
        alias /staging4/fanyucai/web2django/myproject/static;
    }

    location / {
        uwsgi_pass  django;
        include     /staging4/fanyucai/web2django/myproject/uwsgi_params;
    }
}
```
然后建立软链接
```{.cs}
sudo ln -s /staging4/fanyucai/web2django/myproject/mysite_nginx.conf /etc/nginx/sites-enabled/
```