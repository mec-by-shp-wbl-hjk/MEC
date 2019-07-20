from django.shortcuts import render, redirect, render_to_response
from MECboard.models import Board, Comment
import os
import math
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from MECboard.forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout, )

UPLOAD_DIR = "d:/upload/"
login_failure = False

@csrf_exempt
def list(request):
    
    try:
        search_option=request.POST["search_option"]
    except:
        search_option="writer"
    try:
        search=request.POST["search"]
    except:
        search=""
        
    if search_option=="all":
        boardCount=Board.objects.filter(Q(writer__contains=search)
        |Q(title__contains=search)|Q(content__contains=search)).count()
    elif search_option=="writer":
        boardCount=Board.objects.filter(Q(writer__contains=search)).count()
    elif search_option=="title":
        boardCount=Board.objects.filter(Q(title__contains=search)).count()
    elif search_option=="content":
        boardCount=Board.objects.filter(Q(content__contains=search)).count()
       
    try:
        start=int(request.GET["start"])
    except:
        start=0
    page_size = 10
    page_list_size = 10
    end = start + page_size
    total_page = math.ceil(boardCount / page_size)
    current_page=math.ceil( (start+1) / page_size )
    start_page = math.floor( (current_page - 1) / page_list_size)\
        * page_list_size + 1
    end_page = start_page + page_list_size - 1
    
    if total_page < end_page:
        end_page = total_page
    if start_page >= page_list_size:
        prev_list = (start_page - 2) * page_size
    else:
        prev_list = 0
    if total_page > end_page:
        next_list = end_page * page_size
    else:
        next_list = 0
    
    if search_option=="all":
        boardList=Board.objects.filter(Q(writer__contains=search)
        |Q(title__contains=search)|Q(content__contains=search)).order_by("-idx")[start:end]
    elif search_option=="writer":
        boardList=Board.objects.filter(Q(writer__contains=search)).order_by("-idx")[start:end]
    elif search_option=="title":
        boardList=Board.objects.filter(Q(title__contains=search)).order_by("-idx")[start:end]
    elif search_option=="content":
        boardList=Board.objects.filter(Q(content__contains=search)).order_by("-idx")[start:end]
        
    links = []
    for i in range(start_page, end_page+1):
        page = (i-1) * page_size
        links.append("<a href='?start="+str(page)+"'>"+str(i)+"</a>")
        
    if not request.user.is_authenticated:
        username = request.user
        is_authenticated = request.user.is_authenticated
    else:
        username = request.user.username
        is_authenticated = request.user.is_authenticated
    global login_failure
    if login_failure == True:
        login_failure = False
        login_failed = True
    else:
        login_failed = False
    
    return render_to_response("list.html", 
                    {"boardList":boardList, "boardCount":boardCount,
                     "search_option":search_option, "search":search,
                     "range":range(start_page-1, end_page),
                     "start_page":start_page, "end_page":end_page,
                     "page_list_size":page_list_size, "total_page":total_page,
                     "prev_list":prev_list, "next_list":next_list,
                     "links":links, "username":username, "is_authenticated":is_authenticated, "login_failed":login_failed})

def write(request):
    username = request.user
    return render_to_response("write.html", {"username":username})

@csrf_exempt
def insert(request):
    fname=""
    fsize=0
    if "file" in request.FILES:
        file = request.FILES["file"]
        print(file)
        fname = file._name
        
        print(UPLOAD_DIR+fname)
        with open("%s%s" % (UPLOAD_DIR, fname), "wb") as fp:
            for chunk in file.chunks():
                fp.write(chunk)
            
        fsize = os.path.getsize(UPLOAD_DIR+fname)
        
    dto = Board(writer = request.POST["writer"],
                title = request.POST["title"],
                content = request.POST["content"],
                filename = fname, filesize = fsize)
    dto.save()
    return redirect("/")

def download(request):
    id = request.GET["idx"]
    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR+dto.filename
    filename = os.path.basename(path)
    filename=urlquote(filename)
    with open(path, "rb") as file:
        response = HttpResponse(file.read(),
                content_type="application/octet-stream")
        response["Content-Disposition"]=\
        "attachment;filename*=UTF-8''{0}".format(filename)
        dto.down_up()
        dto.save()
    return response
    
def detail(request):
    id = request.GET["idx"]
    username = request.GET["username"]
    is_authenticated = request.GET["is_authenticated"]
    is_superuser = request.user.is_superuser
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    filesize="%.2f" % (dto.filesize / 1024)
    
    commentList=Comment.objects.filter(board_idx=id).order_by("-idx")
    
    return render_to_response("detail.html", 
        {"dto":dto, "filesize":filesize, "commentList":commentList, "username":username, "is_authenticated":is_authenticated, "is_superuser":is_superuser})

@csrf_exempt    
def update_page(request):
    id = request.POST['idx']
    dto = Board.objects.get(idx=id)
    filesize="%.2f" % (dto.filesize / 1024)
    username = request.user
    return render_to_response("update_page.html", {"username":username, "dto":dto, "filesize":filesize})

@csrf_exempt
def update(request):
    id = request.POST["idx"]
    dto_src=Board.objects.get(idx=id)
    
    fname = dto_src.filename
    fsize = dto_src.filesize
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file._name
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        fsize = os.path.getsize(UPLOAD_DIR+fname)
        
    dto_new = Board(idx=id, writer=request.POST["writer"],
        title=request.POST["title"], content=request.POST["content"],
        filename=fname, filesize=fsize, hit=request.POST["hit"])
    dto_new.save()
    return redirect("/")

@csrf_exempt
def delete(request):
    id = request.POST["idx"]
    Board.objects.get(idx=id).delete()
    return redirect("/")

@csrf_exempt
def reply_insert(request):
    id = request.POST["idx"]
    username = request.POST["username"]
    rating = request.POST["rating"]
    is_authenticated = request.POST["is_authenticated"]
    dto = Comment(board_idx=id, writer=request.POST["writer"],
                  content=request.POST["content"], rating=request.POST["rating"])
    dto.save()
    return HttpResponseRedirect("detail?idx="+id+"&username="+username+"&is_authenticated="+is_authenticated+"&rating="+rating)

def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            django_login(request, new_user)
            return redirect("/")
        else:
            return render_to_response("index.html", 
                                      {"msg":"failed to sign up..."})
    else:
        form = UserForm()
        return render(request, "join.html", {"form":form})

def logout(request):
    django_logout(request)
    return redirect("/")

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(username=name, password=pwd)
        if user is not None:
            django_login(request, user)
            return redirect("/")
        else:
            global login_failure
            login_failure = True
            return redirect("/")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form":form})