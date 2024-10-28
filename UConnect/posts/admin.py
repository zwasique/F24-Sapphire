from django.contrib import admin

from .models import UserPost
from .models import User
from .models import UserTagMapping
from .models import UserTags
from .models import Inbox
from .models import Messages

admin.site.register(UserPost)
admin.site.register(User)
admin.site.register(UserTagMapping)
admin.site.register(UserTags)
admin.site.register(Inbox)
admin.site.register(Messages)