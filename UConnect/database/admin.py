from django.contrib import admin

from .models import User
from .models import UserPost
from .models import Tag
from .models import Conversation
from .models import Message


admin.site.register(User)
admin.site.register(UserPost)
admin.site.register(Tag)
admin.site.register(Conversation)
admin.site.register(Message)