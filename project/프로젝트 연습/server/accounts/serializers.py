from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        # get_user_model로 해야 안꼬인다