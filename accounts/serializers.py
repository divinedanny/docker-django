from asyncio import start_unix_server
from site import USER_BASE
from rest_framework import serializers
from .models import User, VerifyUserOtp
from rest_framework.response import Response
from rest_framework import status

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'email', 'firstname', 'lastname']
        
    def create(self, validated_data):
        return super().create(**validated_data)
    
    
class ViewUserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstname', 'lastname']
        
class SendOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyUserOtp
        fields = ['email', 'otp']
    
    def validate(self, attrs):
        try:
            user_email = attrs['email']
            user = User.objects.get(email = user_email)
            if user:
                return user
            else:
                return Response({'Email not Valid'})
            
        except User.DoesNotExist as e:
            return e

class VerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    otp = serializers.CharField(max_length=255)
    
    
    
    