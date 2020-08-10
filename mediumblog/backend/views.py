from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from django.core import serializers
from .models import *
import json

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


class Ajax(View):
    def get(self, request):
        action = request.GET.get('action', None)
        if action == 'countrychange':
            countryid = request.GET.get('countryid', None)
            data = json.loads(serializers.serialize('json', State.objects.filter(country_id=countryid)))
            context = {'data': data}
            return JsonResponse(context)
        context = {'data': 'no data'}
        return JsonResponse(context)

    def post(self, request):
        action = request.POST.get('action', None)
        if action == 'countrychange':
            countryid = request.POST.get('countryid', None)
            data = json.loads(serializers.serialize('json', State.objects.filter(country_id=countryid)))
            context = {'data': data}
            return JsonResponse(context)
        context = {'data': 'no data'}
        return JsonResponse(context)