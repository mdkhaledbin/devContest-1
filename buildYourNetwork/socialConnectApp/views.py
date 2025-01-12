from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from .serializers import userRegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .authentication import generate_access_token, generate_refresh_token, decode_access_token, decode_refresh_token, IsAuthenticatedCustom
from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import JWTAuthentication
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
    

class UserListView( APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    def get(self, request, *args, **kwargs):
        data = User.objects.all()  # Fetch all User objects
        serializer = UserSerializer(data, many=True)  # Serialize the data
        return Response(serializer.data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        queryset = User.objects.get(id=user_id)
        serializer = UserSerializer(queryset, many=False)
        return Response(serializer.data)

class loginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            response =  Response({'message': "Login successful.",
                             'user': UserSerializer(user).data,
                                'access_token': generate_access_token(user),
                                'refresh_token': generate_refresh_token(user)
                             })
            response.set_cookie('refresh_token', generate_refresh_token(user), httponly=True)
            response.set_cookie('access_token', generate_access_token(user), httponly=True)
            return response
        return Response({'message': "Invalid credentials."})

class logoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    
    def post(self, request):
        print('logoutView')
        response = Response({'message': 'Logged out successfully'})
        response.delete_cookie('refresh_token')
        response.delete_cookie('access_token')
        return response
    
