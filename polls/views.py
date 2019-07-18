from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render



def article(request):
    return render(request, 'article.html',)
def message(request):
    leave = Leave.objects.all()
    return render(request, 'message.html',{
        'Leave':leave,
    })
def photo(request):
    album = Album.objects.all()
    return render(request, 'pohot.html',{
        'Album': album,
    })


from django.shortcuts import render, redirect
# 导入分页插件包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 引入模型
from .models import Articles, Users, Category, Album, Leave
# 加密算法的包
import hashlib


# Create your views here.
def index(request):
    # 添加中间导航
    categorys = Category.objects.all()
    articles = Articles.objects.all()
    # 分页的实现
    p = request.GET.get('p')     #  在URL中获取当前的页面数
    paginator = Paginator(articles, 5)    # 对查询的数据对象list进行分离，设置超过5条数据就分页
    try:
        articles = paginator.page(p)    # 获取当前页码的记录
    except PageNotAnInteger:
        articles = paginator.page(1)    # 如果输入的页码不是整数时，显示第1页的内容
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)    # 如果用户输入的页数不在系统的页码列表中时，显示最后一页的内容
    return render(request, 'home.html', {
        'articles': articles,
        'categorys': categorys,
    })


def detail(request):
    # 获取id
    id = request.GET.get('id')
    print(id)
    # 查询id对应的文章
    article = Articles.objects.get(id=id)

    return render(request, 'detail.html', {
        'article': article
    })


def login(request):
    # 写判断
    # 去数据库查，有没有对应的用户
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        ret = Users.objects.filter(username=username, password=password)
        if ret :
            return redirect('/polls/')
        else:
            message = "密码不正确！"
            return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


def register(request):
    # print('aaaaaaaaaaa')
    # 把前端的数据接收过来，保存到数据库
    if request.method == 'POST':
        # 获取前端数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 打印测试
        # print(username, password, password1)
        # 存到数据库
        print("123")
        if username and password:
            # 判断
            # print('OK')
            sha256 = hashlib.sha256(bytes('加一些东西', encoding='utf8') + b'lxgzhw')
            sha256.update(bytes(password, encoding='utf8'))
            password = sha256.hexdigest()
            # 保存到数据库
            ret = Users.objects.create(username=username, password=password)
            if ret:
                # 成功了
                print("succ")
                message = "注册成功请登录！"
                return render(request,'login.html',{"message":message})
            else :
                message = "注册失败！"
                return render(request, 'register.html', {"message": message})
        else:
            print("456")
    return render(request, 'register.html')



