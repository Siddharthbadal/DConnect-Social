from django.contrib import admin
from .models import Room, Topic, GroupMessage

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(GroupMessage)