
from django.contrib import admin
from django.urls import path,include
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh
    path('registration/regional-director/', RegionalDirectorRegisterView.as_view(), name='regional-director-register'),
    path('registration/country-director/', CountryDirectorRegisterView.as_view(), name='country-director-register'),
    path('registration/pf/', PFRegisterView.as_view(), name='pf-register'),
    path('registration/pd',PDRegistrationAPIView.as_view(),name="pd_registration"),
    path('registration/sdr/', SDRRegisterView.as_view(), name='sdr-register'),
    path('registration/health/', HealthRegisterView.as_view(), name='health-register'),
    path('verify-email/', EmailVerifyAPIView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/', PostCommentsListAPIView.as_view(), name='post-comments'),
]