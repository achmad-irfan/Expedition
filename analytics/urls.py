from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'app_analytics'

urlpatterns = [
    path('', views.Analytics.as_view(), name='analytics' ),
]
