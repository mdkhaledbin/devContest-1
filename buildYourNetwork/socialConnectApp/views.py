from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics, status
from .serializers import userRegisterSerializer, UserSerializer, FolloweSerializer
from django.contrib.auth import authenticate
from .authentication import generate_access_token, generate_refresh_token, decode_access_token, decode_refresh_token, IsAuthenticatedCustom
from django.contrib.auth.mixins import LoginRequiredMixin
from .permission import JWTAuthentication

from django.contrib.auth.models import User
from .models import Follower
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
    
class FollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    def post(self, request, user_id):
        follower = request.user
        try:
            following = User.objects.get(id = user_id)
            if(follower == following):
                return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            created = Follower.objects.get_or_create(follower=follower, following=following)
            # if created:
            #     print(created)
            return Response({"message": f"You are now following {following.username}"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
class FollowersListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    
    def get(self, request, user_id):
        try: 
            user = User.objects.get(id = user_id)
            print(user)
            follower = user.followers.all()
            follower=FolloweSerializer(follower, many=True)
            print(follower.data)

            return Response({"me": request.user.id, "followers": list(follower.data)}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
class FollowingListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedCustom]
    
    def get(self, request, user_id):
        try: 
            user = User.objects.get(id = user_id)
            print(user)
            following = user.following.all()
            
            following=FolloweSerializer(following, many=True)
            print(following.data)
            return Response({"me": request.user.id, "following": list(following.data)}, status=status.HTTP_200_OK)
        except:
            return Response({"error": f"{user.username} not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UnfollowView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticatedCustom]
    def post(self, request, user_id):
        try:
            follower = request.user
            following = User.objects.get(id=user_id)
            follow_instance = Follower.objects.filter(follower=follower, following = following)
            if follow_instance.exists():
                follow_instance.delete()
                return Response({'message':f"you {request.user}, have unfollow {user_id} number user."}, status=status.HTTP_200_OK)
            else:
                return Response({'message':f"you {request.user}, are not authenticated to unfollow {user_id} number user.1"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':f"you {request.user}, are not authenticated to unfollow {user_id} number user.2"}, status=status.HTTP_400_BAD_REQUEST)
        
    
            
        