from django.urls import path
from apps.dashboard.views import *

urlpatterns = [
    path('', dashboard, name='dashboard')
]