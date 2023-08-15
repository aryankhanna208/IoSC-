from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import viewsets, generics


from rest_framework.permissions import IsAuthenticated,IsAdminUser, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication


class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if request.method == 'GET':
            return True
        
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser :
                return True
        
        return False

class showEvents(APIView):
     def get(self, request):
        events = Events.objects.all() 
        serializer = EventsSerializer(events, many=True)  

        return Response (serializer.data)
class showProjects(APIView):
     def get(self, request):
        projects = Projects.objects.all() 
        serializer = ProjectsSerializer(projects, many=True)  

        return Response (serializer.data)
     
class showBlogs(APIView):
     def get(self, request):
        blogs = Blog.objects.all() 
        serializer = BlogSerializer(blogs, many=True)  

        return Response (serializer.data)
     

class Event(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]  # Use appropriate authentication classes
    permission_classes = [WriteByAdminOnlyPermission]  # Use IsAuthenticated permission
    serializer_class = EventsSerializer
    queryset = Events.objects.all()
