
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('pd_registration/',PDRegistrationAPIView.as_view(),name="pd_registration"),
]