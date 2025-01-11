from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from .serializers import userRegisterSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializer = userRegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "User registerd successfully.",
                             'user': serializer.data
                             })
        return Response(serializer.errors)
    
class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        data = User.objects.all()  # Fetch all User objects
        serializer = UserSerializer(data, many=True)  # Serialize the data
        return Response(serializer.data)