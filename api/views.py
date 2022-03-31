
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from api import serializers
from django.contrib.auth.models import User
from api import permissions
from api.models import Post,Comment,Category
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from api.permissions import IsOwnerOrReadOnly,IsOwnerOnly
from rest_framework.authentication import TokenAuthentication


# Create your views here.
#List User
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

    permission_class=[IsAuthenticated]

#Retrive User Detail
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

#Getting or Creating Post
class PostListOrCreate(generics.ListCreateAPIView):
    # queryset=Post.objects.all()
    #overriding queryset =>fetching post of currently logged in user
    def get_queryset(self) :
        user = self.request.user
        return Post.objects.filter(owner=user)
        
        
    serializer_class=serializers.PostSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsOwnerOnly]

    #On Creating Username will save
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
#Retrieve,Update,Delete   
class PostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes=[TokenAuthentication,]#if you miss comma,then it will not work
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

#CommentList or Post a comment
class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=serializers.CommentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

