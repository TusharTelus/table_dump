# Create your views here.
from __future__ import unicode_literals

from rest_framework import views
from rest_framework.response import Response
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import LoginSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.http import HttpResponse
import datetime
from django.contrib.auth import  login
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
from django.conf import settings
#from sett import *
# Create your views here.



class ObtainExpiringAuthToken(ObtainAuthToken):

    """View enabling username/password exchange for expiring token."""
    model = Token
    def post(self, request):
        print("heelo")
        """Validate User has valid token or not."""
        username = request.data["username"]
        user_obj = User.objects.get(username=username)
        k = Mapping_Record.object.filter(uuid = "abc")
        k.update(schema =  '{"hgf":"dkdk"}')


        """Respond to POSTed username/password with token and store login history."""
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            token, _ = Token.objects.get_or_create(
                user=serializer.validated_data['user']
            )
            token, created = Token.objects.get_or_create(user=user_obj)

        if user_obj is not None:
            if user_obj.is_active:
                login(request, serializer.validated_data["user"])

            data = {}
            now = datetime.datetime.now()
            data['success'] = True
            data['message'] = 'Logged In Successfully'
            data['auth_key'] = token.key
            data["username"] = username
            return Response(data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Upload_schema(views.APIView):
    def post(self,request):
            schema = request.data["schema"]
            table_id = request.data["table_id"]
            return HttpResponse("hello")

#     if request.method == "POST":
#         return HttpResponse("hello")
#     else:
#         return HttpResponse("error")






