from django.contrib import admin

from .models import UserPost
from .models import User
from .models import UserTagMapping
from .models import UserTag
from .models import Inbox
from .models import Message

admin.site.register(UserPost)
admin.site.register(User)
admin.site.register(UserTagMapping)
admin.site.register(UserTag)
admin.site.register(Inbox)
admin.site.register(Message)