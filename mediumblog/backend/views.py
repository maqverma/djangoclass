from django.shortcuts import render, redirect
from django.views import View
from .models import *

# Create your views here.


class Index(View):
    def get(self, request):
        context = {}
        return render(request, "backend/form.html", context)

    def post(self, request):
        heading = request.POST.get('heading', None)
        content = request.POST.get('content', None)
        articleMode = Article(heading=heading, content=content, image='')
        articleMode.save()
        return redirect('/back/')