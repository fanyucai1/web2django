# 1.如何在登陆网页的时候，设置好默认的用户名与密码，而不需要单独输入？
```{.cs}
 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/django/contrib/admin/templates/admin/login.html myproject/templates/admin/           
```
修改login.html添加JavaScript 代码
```{.cs}
{% extends 'admin/login.html' %}

{% block content %}
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('#id_username').value = 'your_username';
            document.querySelector('#id_password').value = 'your_password';
        });
    </script>
```