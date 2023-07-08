from django.db import models
from users.models import Profile
import uuid


class Topic(models.Model):
    name = models.CharField(max_length=255)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    topic =models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(Profile, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)   # saved on updates
    created_at = models.DateTimeField(auto_now_add=True) # once saved
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-updated', '-created_at']

    def __str__(self):
        return self.name    
    
    

class GroupMessage(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)   # saved on updates
    created_at = models.DateTimeField(auto_now_add=True) # once saved
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-updated', '-created_at']

    def __str__(self):
        return self.body[0:25]
