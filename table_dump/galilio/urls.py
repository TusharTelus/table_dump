from django.urls import path , include
#from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
schema_view = get_swagger_view(title='Pastebin API')
from rest_framework.schemas.coreapi import AutoSchema

urlpatterns = [
    path('',schema_view),
    path('login', views.ObtainExpiringAuthToken.as_view(), name='login'),
    path('upload_schema', views.Upload_schema.as_view(), name='upload_schema'),
]
