from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm, ProfileForm, AccountForm, FilterForm
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

 #i edited this section be sure to verify before adding to main pls i am not sure if its  a real work and not a my machine only work -tyger
def launch(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False) 
            post.save() 

            tags = [
                form.cleaned_data[f'tag_{i}'] 
                for i in range(1, 7) 
                if form.cleaned_data.get(f'tag_{i}')
            ]
            post.tags.set(tags) 

            return HttpResponseRedirect("../home")
    else:
        form = PostForm()  # This initializes the form for a GET request.
    return render(request, 'database/pages/launch.html', {"form": form})

def account(request):
    user = User.objects.get(pk=1) # Note: this is just the first user in the DB for now
    if request.method == "POST":
        form = AccountForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../account")

    else:
        form = AccountForm(initial={"biography": user.biography})

    return render(request, 'database/pages/account.html', {"form": form, "user": user})


# def account(request):
#     user = User.objects.get(pk=1) # For now just retrieves first user in db, ideally we can specify it per request

#     return render(request, "database/pages/account.html", {'user': user})    

#i edited this section be sure to verify before adding to main pls i am not sure if its  a real work and not a my machine only work -tyger
def search(request):
    form = FilterForm(request.POST or None)
    posts = UserPost.objects.all()
    users = User.objects.all()

    if request.method == "POST":
        form = FilterForm(request.POST)

        if form.is_valid():  # Validate the form first
            keywords = form.cleaned_data.get('keywords', "")
            selected_tags = [
                form.cleaned_data.get(f'tag_{i}')
                for i in range(1, 7)
                if form.cleaned_data.get(f'tag_{i}')
            ]

            # Filter posts and users by tags
            if selected_tags:
                posts = posts.filter(tags__in=selected_tags).distinct()
                users = users.filter(tags__in=selected_tags).distinct()

            # Filter by text
            if keywords:
                posts = posts.filter(post_body__icontains=keywords)
                users = users.filter(biography__icontains=keywords)

    return render(request, 'database/pages/search.html', {
        'form': form,
        'posts': posts,
        'users': users,
    })
        #if form.is_valid():
         #if selected_tags:
          #      redirect_path += "tags=" + ",".join([tag.name for tag in selected_tags]) # TODO: Doesn't properly handle multiple , maybe fixed
           #     if search_substring:
            #        redirect_path += "&"
            #
       #     if search_substring:
        #        redirect_path += "text=" + search_substring

         #   return HttpResponseRedirect(redirect_path)

   # else:
    #    form = FilterForm()
     #   tags = request.GET.getlist('tags')
      #  text = request.GET.get('text')

       # posts = UserPost.objects.all()
        #users = User.objects.all()

    #    if tags:
     #       scored_posts = []
      #      scored_users = []

       #     for post in posts:
        #        hit_count = 0
         #       for tag in post.tags.all():
          #          if tag.name in(tags):
           #             hit_count += 1
            #    if hit_count >= 1:
             #       scored_posts.append((post, hit_count))

          #  for user in users:
           #     hit_count = 0
            #    for tag in user.tags.all():
             #       if tag.name in(tags):
              #          hit_count += 1
       #         if hit_count >= 1:
        #            scored_users.append((user, hit_count))

         #   scored_posts.sort(key=lambda x: x[1], reverse=True)
          #  posts = [p[0] for p in scored_posts]

           # scored_users.sort(key=lambda x: x[1], reverse=True)
       #     users = [u[0] for u in scored_users]
        
   #     if text:
    #        start_posts = posts
     #       start_users = users

      #      posts = [p for p in start_posts if text in p.post_body]
       #     users = [u for u in start_users if text in u.biography]

    #return render(request, 'database/pages/search.html', {'form': form, 'posts': posts, 'users': users, 'filter_tags': tags, 'filter_text': text})








# credit: https://medium.com/@biswajitpanda973/how-to-fetch-all-data-from-database-using-django-87d4e1951931