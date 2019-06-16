from django.urls import path
from . import API

urlpatterns = [
    path('test', API.test, name='test'),
]
