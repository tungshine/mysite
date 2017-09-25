from django.shortcuts import render, HttpResponse
from blog import models
from blog.models import User


# Create your views here.


def blog_list(request):
    return render(request, 'blog_list.html', {'books': '111'})


# 注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)

        user_set = User.objects.filter(username=username)
        if len(user_set) == 0:
            models.User.objects.create(
                username=username,
                email=email,
            )
            return render(request, 'register.html', {"msg": "注册成功", "code": 0})
        else:
            return render(request, 'register.html', {"msg": "用户名已存在", "code": -1})
    else:
        return render(request, 'register.html')


def login(request):
    return None


def year_archive(request, year, month):
    return HttpResponse(year + '年' + month + '月')
