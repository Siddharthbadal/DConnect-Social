from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile, Skills, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [ 'email', 'username', 'password1','password2']
        labels ={
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', "placeholder":''})
        

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields ="__all__"
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message 
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
