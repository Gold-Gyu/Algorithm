from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = Todo
        fields = "__all__"
