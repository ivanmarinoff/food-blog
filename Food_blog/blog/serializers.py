from rest_framework import serializers
from .models import Blog, Profile


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'rating']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
