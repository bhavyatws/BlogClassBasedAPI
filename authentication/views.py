from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()



from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class LoginApiView( APIView ):

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.POST['username']).first()

        if user and check_password( request.POST['password'], user.password ):
            obj = Token.objects.filter( user_id=user.pk ).first()
            if not obj:
                obj = Token.objects.create( user=user )
            return Response({
                'token' : obj.key
            })
        else:
            return Response({
                'error' : "Incorrect login credentials"
            })
    
   
        
        