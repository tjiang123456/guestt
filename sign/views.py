from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import request
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    # return HttpResponse("<h1>HELLO Django<h1>")
    return render(request,"index.html")

#登录请求
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username","")
        login_password = request.POST.get("password","")
        user = auth.authenticate(username=login_username,password=login_password)
        if login_username== "" or login_password =="":
            return render(request, "index.html",
                          {"error":"用户名密码为空"})
        # if username != "admin" or password!="admin123":
        #     return render(request, "index.html",
        #                   {"error": "用户名或密码错误"})
        if user is not None:
            auth.login(request,user)#登录
            response = HttpResponseRedirect('/event_manage/')
            request.session['user'] = login_username  #添加浏览器session
            return response
        else:
            return render(request, "index.html",
                              {"error": "用户名或密码错误"})
            # response.set_cookie('user',username,3600)
    else:
        #重定向到根路径
        return HttpResponseRedirect('/')

@login_required
def event_manage(request):
    #如果取不到cookie的话默认会得到一个空串
    # username = request.COOKIES.get('user','')
    username = request.session.get('user','') #读取浏览器session
    return render(request, 'event_manage.html',{'user':username})