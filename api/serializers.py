from dataclasses import fields
from http import server

from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post,Comment,Category

class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=User
        fields=['id','username','posts','comments','categories']

class PostSerializer(serializers.ModelSerializer):
    #this return username ,if owner not given by default id will be passed instead of owner
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    owner=serializers.ReadOnlyField(source='owner.username')
    comments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Post
        fields=['id','title','body','owner','comments','categories','created']

#Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Comment
        fields = ['id', 'body', 'owner', 'post']

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']
