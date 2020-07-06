  
from django.shortcuts import render
from .logic import *
from .models import Shortcut
from django.core.paginator import Paginator


def index(request):
    session_clear(request)
    if request.method == "POST":
        show_lists = Logic.get_list(request)
    return render(request, 'web/index.html')

def show_list(request):
    print("list")
    show_lists = Logic.get_list(request)
    paginator = Paginator(show_lists, 10)
    return render(request, "web/list.html",{'short_lists': show_lists})

def show_list_1(request):
    session_clear(request)
    show_list(request)
    

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

def delete(request):
    session_clear(request)
    return redirect("/list/")

def test(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/test.html',{"result":"fail"})

def session_clear(request):
    if request.session.get('os', False) or request.session.get('program', False) or request.session.get('searchValue', False):
        request.session.clear()