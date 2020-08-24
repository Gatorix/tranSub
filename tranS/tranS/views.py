from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world")


def runoob(request):
    views_name = "tranSub"
    return render(request, "runoob.html", {"name": views_name})


def tranS(request):
    view_list = ["111", "222", "333"]
    return render(request, "tranS.html", {"view_list": view_list})
