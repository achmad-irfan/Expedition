from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'app_tracking'

urlpatterns = [
    path('', views.Tracking.as_view(), name='tracking' ),
]
