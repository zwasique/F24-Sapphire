from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm, ProfileForm
from .models import User, UserPost


def login(request):
    return render(request, 'database/pages/login.html', {})

def home(request):
    return render(request, 'database/pages/home.html', {})

def posts(request):
    return render(request, 'database/pages/posts.html')

def account(request):
    return render(request, 'database/pages/account.html')

def inbox(request):
    return render(request, 'database/pages/inbox.html')

def profile_form(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../home") # Note: Use URLs based on urls.py rather than directly referencing html files
        
    else:
        form = ProfileForm()
    
    return render(request, "database/pages/signup.html", {"form": form})


def launch(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../home")

    else:
        form = PostForm()

    return render(request, 'database/pages/launch.html', {"form": form})


def profile(request):
    # ChatGPT code start
    user = User.objects.get(pk=1)

    context={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'biography': user.biography
    }
    # ChatGPT code end

    return render(request, "database/pages/profile.html", {'profile': context})    

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/") # eventually want this to be search page

    else:
        form = PostForm()

    return render(request, "database/pages/searching.html", {"form": form})

def search(request):
    post_list = UserPost.objects.all()
    return render(request, 'database/pages/search.html',
                  {'post_list': post_list})


def display_users(request):
    users = User.objects.all()
    return render(request, 'database/pages/account.html', {'users': users})
# credit: https://medium.com/@biswajitpanda973/how-to-fetch-all-data-from-database-using-django-87d4e1951931


def display_posts(request):
    posts = UserPost.objects.all()
    users = User.objects.all()
    return render(request, 'database/pages/search.html', {'posts': posts, 'users': users})

