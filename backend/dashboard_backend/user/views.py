from user.models import User
from .serializers import UserSerializer
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListView(APIView):
    """
    Get user list
    """

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # Create User
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    """
    Get User detail, update user detail
    """

    def get(self, request, id, format=None):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except user.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
