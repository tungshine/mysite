# __author: TungShine
# __date: 2017/9/26
# __description:

from django.conf.urls import url
from blog import views

urlpatterns = {

    url(r'^books$', views.blog_list),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    # 在正则表达式中添加“()”，可以在视图函数中直接取到这个参数的值, 其中几个“()”就要几个参数来接收
    # url(r'^(articles)/([0-9]{4})/$', views.year_archive),
    # 加上?P<param>的样式，是将要接收的参数取了param参数的名字
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.year_archive),

}
