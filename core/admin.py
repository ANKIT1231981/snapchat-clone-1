from django.contrib import admin
from .models import FriendRequest, Message, Chat, SnapUser, MyUserAdmin

# Register your models here.
admin.site.register(FriendRequest)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(SnapUser, MyUserAdmin)
