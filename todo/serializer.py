from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model


User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'



class UserSerialzier(serializers.ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'