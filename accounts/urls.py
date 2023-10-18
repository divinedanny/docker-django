from django.urls import path
from accounts.views import RegisterUserView, ViewUserView, VerifyOtpView

app_name = "accounts"

urlpatterns = [
    path('create-user/', RegisterUserView.as_view(), name='create_user'),
    path('view-user/<int:id>/', ViewUserView.as_view(), name='view_user'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify-otp')
]

