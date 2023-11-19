from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import *

# create your views here

@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/")
    else:
        form = PostForm()

    return render(request, 'create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/signup.html', {"form": form})

@login_required(login_url="/login")
def details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'details.html', {"post": post})
