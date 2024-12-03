from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm, ProfileForm
from .models import User
from .models import UserPost

def login(request):
    return render(request, 'database/pages/login.html', {})

def home(request):
    return render(request, 'database/pages/home.html', {})

def posts(request):
    return render(request, 'database/pages/posts.html')

def inbox(request):
    return render(request, 'database/pages/inbox.html')


def signup(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../home") #will redirect to the home page if form is valid, however, this doesn't work right now
        
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


def account(request):
    user = User.objects.get(pk=1) # For now just retrieves first user in db, ideally we can specify it per request

    return render(request, "database/pages/account.html", {'user': user})    


def search(request):
    posts = UserPost.objects.all()
    users = User.objects.all()
    return render(request, 'database/pages/search.html', {'posts': posts, 'users': users})
# credit: https://medium.com/@biswajitpanda973/how-to-fetch-all-data-from-database-using-django-87d4e1951931
