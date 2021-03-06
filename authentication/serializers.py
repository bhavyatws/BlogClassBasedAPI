from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
'''
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','password2',]
        extra_kwargs={
            'first_name':{'required':True},
            'last_name':{'required':True},
        }
    def validate(self,attrs):#this function name must be validate
        # print(attrs['password'])
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Both password should be same'})
        return attrs

    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
'''

class RegisterSerializer(serializers.ModelSerializer):
    # password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    # password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']
    # def validate(self,attrs):#this function name must be validate
        
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({'password':'Both password should be same'})
    #     return attrs
   
    