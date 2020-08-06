from django.shortcuts import render, redirect
from django.views import View
from backend.models import *
# Create your views here.


class Index(View):
    def get(self, request):
        alldata = Article.objects.all()
        context = {'data': alldata, 'user': ''}
        return render(request, "frontend/blogpage.html", context)

    def post(self, request):
        pass


class Login(View):
    def get(self, request):
        context = {'error': ''}
        return render(request, "frontend/login.html", context)

    def post(self, request):
        eorm = request.POST.get('emailormobile', None)
        passn = request.POST.get('pass', None)

        ddata = User.objects.filter(email=eorm, password=passn)
        if not ddata:
            context = {'error': 'User Does not exists.'}
            return render(request, "frontend/login.html", context)
        else:
            context= {'user': ddata[0].fullname}
            return render(request, "frontend/blogpage.html", context)


class Register(View):
    def get(self, request):
        context = {'data': ''}
        return render(request, "frontend/register.html", context)

    def post(self, request):
        name = request.POST.get('name', None)
        mobile = request.POST.get('mobile', None)
        email = request.POST.get('email', None)
        pass1 = request.POST.get('pass1', None)
        pass2 = request.POST.get('pass2', None)

        userSave = User(fullname=name, email=email, mobile=mobile, photo='', password=pass1)
        userSave.save()
        return redirect('/login/')