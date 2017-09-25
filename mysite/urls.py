"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = {

    url(r'^admin/', admin.site.urls),
    url(r'^books', views.blog_list),
    url(r'^register', views.register),
    url(r'^login', views.login),

    # 在正则表达式中添加“()”，可以在视图函数中直接取到这个参数的值, 其中几个“()”就要几个参数来接收
    # url(r'^(articles)/([0-9]{4})/$', views.year_archive),
    # 加上?P<param>的样式，是将要接收的参数取了param参数的名字
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.year_archive),
}
