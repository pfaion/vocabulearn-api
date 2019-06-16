from django.urls import path, include
from . import auth_tools

urlpatterns = [
    path('token', auth_tools.token, name='token'),
    path('v1/', include('api.v1.urls')),
]
