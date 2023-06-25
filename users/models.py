from django.db import models
from django.contrib.auth.models import User 
import uuid 




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username= models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    short_intro = models.CharField(max_length=500)
    bio = models.TextField()
    profile_image= models.ImageField(null=True, blank=True, upload_to='profiles', default='profiles/default.png')
    social_github = models.CharField(max_length=255, null=True, blank=True)
    social_linkedin = models.CharField(max_length=255, null=True, blank=True)
    social_portfolio = models.CharField(max_length=255, null=True, blank=True)
    social_youtube = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.user.username
    


class Skills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name}"



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipent = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    subject= models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    is_read= models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    read_at = models.DateTimeField(auto_now_add=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created_at']