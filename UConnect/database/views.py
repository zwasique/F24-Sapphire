from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProfileForm
from .models import User

def home(request):
    return render(request, 'database/home.html', {})

def profile_form(request):
    if request.method == "POST":
        first_name = ProfileForm.first_name(request.POST)
        last_name = ProfileForm.last_name(request.POST)
        user_biography = ProfileForm.biography(request.POST)

        if form.is_valid():
            User.first_name = first_name
            User.last_name = last_name
            User.biography = user_biography
            return HttpResponseRedirect("/profile/") #will redirect to the profile page if form is valid
        
    else:
        form = ProfileForm()
    
    return render(request, "database/profilecreation.html", {"form": form})

def profile(request):
    first_name = User.objects.get(pk=3)
    last_name = User.objects.get(pk=4)
    biography = User.objects.get(pk=5)

    context={
        'first_name':first_name,
        'last_name':last_name,
        'biography':biography
    }

    return render(request, "database/profile.html", {'profile': context})    
