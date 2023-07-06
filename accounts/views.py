import random
from django.shortcuts import render
from .models import User, VerifyUserOtp
from .serializers import (
    ViewUserInformationSerializer,
    CreateUserSerializer,
    SendOtpSerializer,
    VerifyUserSerializer,
)
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        data = serializer.data
        
        return Response(data, status=status.HTTP_201_CREATED)
    
class ViewUserView(generics.RetrieveAPIView):
    serializer_class = ViewUserInformationSerializer
    
    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = self.get_serializer(user)
        data = serializer.data
        
        return Response(data, status=status.HTTP_200_OK)
        

class SendOtpView(generics.GenericAPIView):
    serializer_class = SendOtpSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request['email']
        user = VerifyUserOtp.objects.get(email=email)
        serializer.is_valid(raise_exception=True)
        otp_pin = ''.join(str([random.randint(0,9) for i in range(6)]))
        user.otp = otp_pin
        user.save()
        
        return Response({'Email has been sent, please check your email or spam section to get the email. Thank you.'})
        
        
class VerifyOtpView(generics.GenericAPIView):
    serializer_class =  VerifyUserSerializer
    
    
    def post(self, request, email):
        serializer = self.serializer_class(data=request.data)
        
        user = VerifyUserOtp.objects.get(email=email)
        if user.email:
            if serializer.otp == user.otp:
                return Response({'Your Accounts has been verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'Wrong OTP, please enter correct OTP'}, status=status.HTTP_400_BAD_REQUEST)