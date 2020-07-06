  
from django.shortcuts import render
from .logic import *
from .models import Shortcut
from django.core.paginator import Paginator


def index(request):
    if request.session.get('os', False) or request.session.get('program', False) or request.session.get('searchValue', False):
        request.session.clear()
    if request.method == "POST":
        show_lists = Logic.get_list(request)
    return render(request, 'web/index.html')

def show_list(request):
    print("list")
    show_lists = Logic.get_list(request)
    paginator = Paginator(show_lists, 10)
    return render(request, "web/list.html",{'short_lists': show_lists})

def show_list_1(request):
    print("list1")
    if request.session.get('os', False) or request.session.get('program', False) or request.session.get('searchValue', False):
        request.session.clear()
    show_lists = Logic.get_list(request)
    paginator = Paginator(show_lists, 10)
    return render(request, "web/list.html",{'short_lists': show_lists})
    

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

def delete(request):
    if request.session.get('os', False) or request.session.get('program', False) or request.session.get('searchValue', False):
        request.session.clear()
    return redirect("/list/")

def test(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/test.html',{"result":"fail"})