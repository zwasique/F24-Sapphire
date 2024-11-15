"""
URL configuration for UConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.login, name="login"),
    path('pages/signup', views.profile_form, name="profile_form"),
    path('pages/account/', views.profile, name="profile"),
    path('pages/launch/', views.create_post, name="create_post"),
    path('pages/searching/', views.posts, name="posts"),
    path('pages/launch/', views.launch, name="launch"),
    # path('pages/inbox/', views.inbox, name="inbox"),
    path('pages/home', views.home, name="home")

]
