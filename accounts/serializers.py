from django.db.models import fields
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email    = validated_data['email'],
            name     = validated_data['name'],
            password = validated_data['password'],
        )

        return user
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'is_admin']

        