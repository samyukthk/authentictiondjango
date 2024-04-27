from django.shortcuts import render
from rest_framework.decorators import api_view, APIView

# Create your views here.
from userapp.models import *
from userapp.serialisers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# from userproject.userapp.serialisers import UserSerializer
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError

# class Signup(APIView):
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = serializer.instance
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Signup(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            user = serializer.save() 
            user.is_user = True  # Set is_user to True here
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# class TeamLeadSignup(APIView):
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Teamlead = serializer.instance
#             Teamlead = serializer.save() 
#             Teamlead.is_teamlead = True  # Set is_user to True here
#             Teamlead.save()
#             token, created = Token.objects.get_or_create(Teamlead=Teamlead)
#             return Response({"Teamlead": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, format=None):
        data = request.data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user:
            serializer = UserSerializer(user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key,"message":"hi"}, status=status.HTTP_200_OK)
        return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

# class TestView(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, format=None):
#         user = request.user
#         serialized_user = UserSerializer(user).data
#         return Response({"user": serialized_user, "message": "Test view"})

class TestView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return Response({"user":user_data, "message": "hi this is user"})

class Logout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            raise ValidationError("User has no auth_token.")
        logout(request)
        return Response({"message": "Logout was successful."})