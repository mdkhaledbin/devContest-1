from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import userRegisterSerializer
# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializer = userRegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "User registerd successfully."})
        return Response(serializer.errors)
