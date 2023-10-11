from user.models import *
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    legal_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, max_length=256)
    email = serializers.CharField(required=True, allow_blank=False, max_length=50)
    salt = serializers.CharField(required=True, allow_blank=False, max_length=10)

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data
        """
        return User.objects.create(**validated_data)
