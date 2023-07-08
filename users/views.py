from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utilis import searchProfiles, paginateProjects
from .models import Profile, Message
from groups.models import Room, GroupMessage
from .forms import CustomUserCreationForm, ProfileUpdateForm, SkillsForm, MessageForm



def userRegister(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # commit keeps a temp object of user
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.info(request, 'Account created! Please login')
            # login(request, user)  #direct login
            return redirect('userlogin')
        # else:
        #     messages.info(request, 'Something is wrong. Try again.')

    context = {'form':form, 'page':page}
    return render(request, 'users/login_register.html', context)




def userLogin(request):
    page = 'login'

    # no login page access if loggedin
    if request.user.is_authenticated:
        return redirect('profiles')

    # check user details
    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        # user = user.objects.get(username=username)
        # try:
        #     user = user.objects.get(username=username)
        # except:
        #     messages.error(request, 'Username does not exists')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'useraccount')
        else:
            messages.error(request, "username or password is incorrect!")
    return render(request, 'users/login_register.html')



def userLogOut(request):
    logout(request)
    messages.info(request, 'You have logged Out!')        
    return redirect('projects')



def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProjects(request, profiles, 6)

    context = {'custom_range':custom_range,'profiles': profiles, 'search_query':search_query}
    return render(request, 'users/home.html', context)


def userProfile(request,pk):
    profile = get_object_or_404(Profile, id=pk)
    mainSkills = profile.skills_set.exclude(description__exact='')
    otherSkills = profile.skills_set.filter(description='')
    rooms = profile.room_set.all()
    room_messages= profile.groupmessage_set.all()

    context = {
        'profile':profile,
        'mainSkills':mainSkills,
        'otherSkills':otherSkills,
        'rooms': rooms,
        'room_messages': room_messages
        }
    return render(request, 'users/userProfile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skills_set.all()
    projects = profile.project_set.all()
    rooms = profile.room_set.all()
    context={
            'profile' : profile,
            'skills': skills,
            'projects':projects ,
            'rooms': rooms        
             }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def update_account(request):
    profile = request.user.profile
    form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('useraccount')
    context = {'form': form}
    return render(request, 'users/update_profile.html', context)


@login_required(login_url='userlogin')
def createSkills(request):
   profile = request.user.profile
   form = SkillsForm()
   if request.method == 'POST':
       form = SkillsForm(request.POST)
       if form.is_valid():
           skill = form.save(commit=False)
           skill.owner = profile
           skill.save()
           messages.success(request, 'Skill added!')
           return redirect('useraccount')
       
   context = {'form': form}
   return render(request, 'users/skill_form.html', context)



@login_required(login_url='userlogin')
def updateSkills(request, pk):
   profile = request.user.profile
   skill = profile.skills_set.get(id=pk)
   print(skill.id)
   form = SkillsForm(instance=skill)

   if request.method == 'POST':
       form = SkillsForm(request.POST, instance=skill)
       if form.is_valid():
           skill.save()
           messages.success(request, 'Skill updated!')
           return redirect('useraccount')
       
   context = {'form': form}
   return render(request, 'users/skill_form.html', context)


@login_required(login_url='userlogin')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.info(request, f'{skill} removed from your skills!')
        return redirect('useraccount')
    context ={'object': skill}
    return render(request, 'delete_template.html', context)



@login_required(login_url='userlogin')
def inbox(request):
    profile = request.user.profile 
    messageRequests = profile.messages.all()
    unReadCount = messageRequests.filter(is_read=False).count()
    context = {
        'messageRequests':messageRequests,
        'unReadCount':unReadCount
    }
    return render(request, 'users/inbox.html', context)


@login_required(login_url='userlogin')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read=True        
        message.save()
    context ={
        'message': message

    }
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    print('recipient', recipient)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None 

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.sender = sender
            print('message.sender', message.sender)
            message.recipent = recipient
            print('message.recipient', message.recipent)

            if sender:
                message.name = sender.name                
                message.email = sender.email 
                
            message.save()
            print(message)

            messages.success(request, 'Your message wass sent successfullt!')
            return redirect('userprofile',pk=recipient.id )

    context = {
        'recipient': recipient,
        'form':form
    }
    return render(request, 'users/message_form.html', context)