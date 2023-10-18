import random
import stat
from rest_framework.response import Response
from .models import UserAccount, VerifyUserOtp
from .serializers import (
    ViewUserInformationSerializer,
    CreateUserSerializer,
    # SendOtpSerializer,
    VerifyUserSerializer,
)
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .tasks import send_otp

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
         #saving the user information and OTP to the database
        user = serializer.save()
        
        #sending the otp to the user
        otp = random.randint(100000, 999999)
        VerifyUserOtp.objects.create(user=user, otp=otp)
        email = request.data['email']
        send_otp.delay(email, otp)
        
        data = serializer.data
        
        return Response(data, status=status.HTTP_201_CREATED)
    
class ViewUserView(generics.RetrieveAPIView):
    serializer_class = ViewUserInformationSerializer
    
    def get(self, request, id):
        user = UserAccount.objects.get(id=id)
        serializer = self.get_serializer(user)
        data = serializer.data
        
        return Response(data, status=status.HTTP_200_OK)
        

# class SendOtpView(generics.GenericAPIView):
#     serializer_class = SendOtpSerializer
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             email = request['email']
#             user = VerifyUserOtp.objects.get(email=email)
#             serializer.is_valid(raise_exception=True)
#             otp_pin = ''.join(str([random.randint(0,9) for i in range(6)]))
#             user.otp = otp_pin
#             user.save()
#             send_otp.delay(email, otp_pin)
        
#             return Response({'Email has been sent, please check your email or spam section to get the email. Thank you.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'Email not availible'})
        
class VerifyOtpView(generics.GenericAPIView):
    serializer_class =  VerifyUserSerializer
    
    
    def post(self, request, email):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user_otp = VerifyUserOtp.objects.get(email=email)
            if user_otp.email:
                if request.data['otp'] == user_otp.otp:
                    UserAccount.is_active = True
                    UserAccount.is_verified = True
                    return Response({'Your Accounts has been verified'}, status=status.HTTP_200_OK)
                elif UserAccount.is_active == True and UserAccount.is_verified == True:
                    return Response({'Your account has already been activated'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'Wrong OTP, please enter correct OTP'}, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response({"User is not availible or Does not exist!!"})