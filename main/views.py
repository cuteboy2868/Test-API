from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
def index_view(request):
    context = {
        'banner': Banner.objects.all().order_by('-id')[:3],
        'products': Product.objects.all().order_by('-id')[:3],
        'about': About_company.objects.last(),
        'news': Blog.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index_2.html', context)


def about_view(request):
    return render(request, 'about.html')


def news_page_view(request):
    return render(request, 'news.html')


def contact_view(request):
    return render(request, 'contact.html')


def shop_page_view(request):
    return render(request, 'shop.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request,'login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request,'register.html')



def profile_view(request, pk):
    user = User.objects.get(pk=pk)
    context ={
        'user': user
    }
    return render(request, 'my-profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_user_url')


def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('login_user_url')





