from rest_framework import serializers
from .models import UserAccount, VerifyUserOtp
from rest_framework import status

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [ 'id', 'email', 'password', 'firstname', 'lastname']
        
    def create(self, validated_data):
        user = UserAccount.objects.create_user(**validated_data)
        return user
    
    
class ViewUserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'firstname', 'lastname']
        
# class SendOtpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VerifyUserOtp
#         fields = ['email', 'otp']
    
    

class VerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    otp = serializers.CharField(max_length=255)
    
    # def validate(self, attrs):
    #     try:
    #         user_email = attrs['email']
    #         user = User.objects.get(email=user_email)
    #         if user:
    #             return user
    #         else:
    #             return Response({'Email not Valid'})

    #     except User.DoesNotExist as e:
    #         return e
    
    
    