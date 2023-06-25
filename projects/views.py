from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Project, Review, Tag 
from .forms import ProjectForm, ReviewForm
from .utilis import searchProjects, paginateProjects
from django.contrib import messages

def projects(request):
   # projects = Project.objects.all().order_by('-created_at')
   projects, search_query = searchProjects(request)
   custom_range, projects = paginateProjects(request, projects, 6)
   
   context ={
            'projects': projects,
            'search_query':search_query,
           
            'custom_range':custom_range
   }

   return render(request, "projects/projects.html", context)  


def project(request, pk):
   project = Project.objects.get(id=pk)
   tags = project.tags.all()
   form = ReviewForm()
   if request.method == 'POST':
      form = ReviewForm(request.POST)
      review = form.save(commit=False)
      review.project = project
      review.owner = request.user.profile 
      review.save()
      project.getVoteCount
      messages.success(request, 'Review submitted successfully!')
      return redirect('project', pk=project.id)

   context ={
      'project': project,
      'tags': tags,
      'form': form
   }
   return render(request, "projects/one-project.html", context)  

@login_required(login_url='userlogin')
def createProject(request):
   profile = request.user.profile
   form = ProjectForm()
   if request.method == 'POST':
      form = ProjectForm(request.POST, request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.owner = profile
         project.save()
         return redirect('projects')
   context ={'form':form}
   return render(request, "projects/project_form.html", context)


@login_required(login_url='userlogin')
def updateProject(request, pk):
   profile = request.user.profile
   project = profile.project_set.get(id=pk)
   form = ProjectForm(instance = project)

   if request.method == 'POST':
      form = ProjectForm(request.POST, request.FILES, instance=project)
      if form.is_valid():
         form.save()
         return redirect('projects')
      
   context ={'form':form}
   return render(request, "projects/project_form.html", context)


@login_required(login_url='userlogin')
def deleteProject(request, pk):
   profile = request.user.profile
   project = profile.project_set.get(id=pk)
   if request.method == 'POST':
      project.delete()
      return redirect('projects')
   context = {'object': project}
   return render(request, "delete_template.html", context)
 
