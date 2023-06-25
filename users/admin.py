from django.contrib import admin
from .models import Profile, Skills, Message

class ProfileAdmin(admin.ModelAdmin):
    list_display=['username', 'name', 'email', 'created_at']

class SkiilsAdmin(admin.ModelAdmin):
    list_display= ['owner', 'name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skills, SkiilsAdmin)
admin.site.register(Message)