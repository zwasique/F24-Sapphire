from datetime import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .forms import PostForm, ProfileForm, MessageForm
from .models import User, UserPost, Conversation, Message


def login(request):
    return render(request, 'database/pages/login.html', {})

def home(request):
    return render(request, 'database/pages/home.html', {})

def posts(request):
    return render(request, 'database/pages/posts.html')

def account(request):
    return render(request, 'database/pages/account.html')

def inbox(request): 
    user = User.objects.get(id=request.user.id) #get user
    #show convos whether you sent or received msg... sender is defined by convo as seeker, recipient is defined by convo as launcher
    conversation = Conversation.objects.filter(Q(seeker_id = user) | Q(launcher_id = user))

    selected_conv = None 
    messages = []

    #when user selects specific chat
    if request.GET.get('conversation_id'):
        conversation_id = request.GET.get('conversation_id')
        selected_conv = get_object_or_404(Conversation, id=conversation_id) #get convo. if doesn't exist, 404
        messages = selected_conv.get_message()
    
    #get all messages
    if not selected_conv:
        inbox = user.get_messages()

    #connect!
    if request.method == 'POST' and selected_conv:
        form = MessageForm(request.POST)

        if form.is_valid():
            message_content = form

        message = Message(
            conversation_id = selected_conv,
            sender = user,
            recipient = selected_conv.launcher_id,
            subject = selected_conv.post_id.project_name,
            time_sent = timezone.now(),
            message_content = message_content
        )
        message.save()
    
        #send user back to convo after sending message
        return HttpResponseRedirect(f'?conversation_id={selected_conv.id}')

    return render(request, 'database/pages/inbox.html', {
        "inbox": conversation,
        "selected_conversation": selected_conv,
        "messages": messages,
    })

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

