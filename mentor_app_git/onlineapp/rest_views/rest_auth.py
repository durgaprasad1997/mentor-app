from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from onlineapp.models import Colleges
from onlineapp.rest_views.Serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import jwt, json
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User

#
# class Login(views.APIView):
#
#     def post(self, request, *args, **kwargs):
#         if not request.data:
#             return Response({'Error': "Please provide username/password"}, status="400")
#
#         username = request.data['username']
#         password = request.data['password']
#         try:
#             user = User.objects.get(username=username, password=password)
#         except User.DoesNotExist:
#             return Response({'Error': "Invalid username/password"}, status="400")
#         if user:
#             payload = {
#                 'id': user.id,
#                 'email': user.email,
#             }
#             jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
#
#         return HttpResponse(
#             json.dumps(jwt_token),
#             status=200,
#             content_type="application/json"
#             )
#
