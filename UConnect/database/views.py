from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProfileForm
from .forms import CreatePost
from .models import User

def home(request):
    return render(request, 'database/home.html', {})

def profile_form(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/") #will redirect to the profile page if form is valid
        
    else:
        form = ProfileForm()
    
    return render(request, "database/profilecreation.html", {"form": form})

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

    return render(request, "database/createpost.html", {"form": form})