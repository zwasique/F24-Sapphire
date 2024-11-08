from django.shortcuts import render
from .models import UserPost

def home(request):
    return render(request, 'database/home.html', {})


def search(request):
    post_list = UserPost.objects.all()
    return render(request, 'database/search.html',
                  {'post_list': post_list})