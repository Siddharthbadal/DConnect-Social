from django.shortcuts import render, redirect
from .models import Room, Topic, GroupMessage
from .forms import RoomForm
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def projectRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages= GroupMessage.objects.filter(Q(room__topic__name__icontains=q))[0:15]

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'room_messages':room_messages
    }
    return render(request, 'groups/rooms.html',context)


def projectRoom(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.groupmessage_set.all().order_by('-created_at')
    participants = room.participants.all()

    if request.method == 'POST':
        groupmessage = GroupMessage.objects.create(
            user = request.user.profile,
            room= room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user.profile)
        return redirect('projectroom', pk=room.id)
    
    context = {
                'room': room,
                'room_messages': room_messages,
                'participants': participants
            }
    return render(request, 'groups/room.html', context )



@login_required(login_url='userlogin')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
               
        if form.is_valid():

            room = form.save(commit=False)
            room.host = request.user.profile
            room.save()
            messages.success(request, 'Room created successfully!')
            return redirect('projectrooms')

    context ={'form': form}
    
    return render(request, 'groups/room_form.html', context)


@login_required(login_url='userlogin')
def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if request.user.profile != room.host:
        messages.success(request, 'This is not your room!')            
        return redirect('projectrooms') 


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
               
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated successfully!')     
            return redirect('projectrooms')
    context = {
        'form': form
    }
    return render(request, 'groups/room_form.html' , context)

@login_required(login_url='userlogin')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('projectrooms')
    return render(request, 'groups/delete.html', {'obj':room})



@login_required(login_url='userlogin')
def deleteMessage(request, pk):
   
    message = GroupMessage.objects.get(id=pk)
    

    if request.method == 'POST':
        message.delete()
        
        return redirect('projectrooms')
    return render(request, 'groups/delete.html', {'obj':message})




