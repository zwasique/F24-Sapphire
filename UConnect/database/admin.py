from django.contrib import admin

from .models import (Conversation, Message, PostTagMapping, Tag, User,
                     UserPost, UserTagMapping)

admin.site.register(User)
admin.site.register(UserPost)
admin.site.register(Tag)
admin.site.register(UserTagMapping)
admin.site.register(PostTagMapping)
admin.site.register(Conversation)
admin.site.register(Message)