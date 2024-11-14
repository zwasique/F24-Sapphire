from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProfileForm
from .forms import CreatePost
from .models import User
from .models import UserPost

def home(request):
    return render(request, 'database/Index.html', {})

def posts(request):
    return render(request, 'database/posts.html')

def launch(request):
    return render(request, 'database/launch.html')

def profile_form(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../database/Index.html") #will redirect to the home page if form is valid, however, this doesn't work right now
        
    else:
        form = ProfileForm()
    
    return render(request, "database/pages/signup.html", {"form": form})

def profile(request):
    # ChatGPT code start
    user = User.objects.get(pk=1)

    context={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'biography': user.biography
    }
    # ChatGPT code end

    return render(request, "database/profile.html", {'profile': context})    

def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/") # eventually want this to be search page

    else:
        form = CreatePost()

    return render(request, "database/searching.html", {"form": form})

def search(request):
    post_list = UserPost.objects.all()
    return render(request, 'database/search.html',
                  {'post_list': post_list})
