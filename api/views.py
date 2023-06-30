from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag 
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'GET': '/api/projects'
        },
        {
            'GET': '/api/projects/id'
        },
        {
            'POST': '/api/projects/id/vote'
        },
        {
            'POST': '/api/user/token'
        },
        {
            'POST': '/api/user/token/refresh'
        },
        
    ]
    
    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# one project
@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects)
    return Response(serializer.data)



@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id = pk)
    user = request.user.profile
    data = request.data 

    review, created = Review.objects.get_or_create(
        owner= user,
        project= project,

    )
    review.value = data['value']
    review.save()
    project.getVoteCount


    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectid = request.data['project']

    project = Project.objects.get(id=projectid)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag deleted!')