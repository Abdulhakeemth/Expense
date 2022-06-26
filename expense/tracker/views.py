from django.shortcuts import render
from django.http import QueryDict
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile,Expense
from rest_framework.filters import SearchFilter
from .serializers import ProfileSerializer,ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import viewsets,serializers
from django.contrib.auth.models import User

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only =True,
        min_length = MIN_LENGTH,
         error_messages={
            "min_length": f"Password must be longer than{MIN_LENGTH} characters."
        }
    )
    password2 = serializers.CharField(
        write_only =True,
        min_length = MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than{MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = User
        fields = "__all__"


    def validate(self , data):
        if data["password"] != data["password2"]:
           raise serializers.validationError("Password does not match.")
        return data

    def create(self,validated_data):
        user  = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"], 

        )  
        user.set_password(validated_data["password"])
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer        

class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user']
    permission_classes = [IsAuthenticated]


    def list(self,request):
        queryset= Profile.objects.all()
        serializer = ProfileSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrive(self,request,pk,id=id):
        id=pk
        if id is not None:
            queryset=Profile.objects.get(id=id)
            serializer = ProfileSerializer(queryset)
        return Response(serializer.data)
    def create(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'successfully Created '},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk
        queryset= Profile.objects.get(pk=id)
        serializer = ProfileSerializer(queryset,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'message':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id=pk
        queryset=Profile.objects.get(pk=id)
        serializer = ProfileSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    def destroy(self,request,pk):
        id=pk
        queryset= Profile.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Data Deleted'})             


class ExpenseViewset(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id']
    permission_classes = [IsAuthenticated]


    def list(self,request):
        queryset= Expense.objects.all()
        serializer = ExpenseSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrive(self,request,pk,id=id):
        id=pk
        if id is not None:
            queryset=Expense.objects.get(id=id)
            serializer = ExpenseSerializer(queryset)
        return Response(serializer.data)
    def create(self,request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'successfully Created '},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk
        queryset= Expense.objects.get(pk=id)
        serializer = ExpenseSerializer(queryset,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'message':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id=pk
        queryset=Expense.objects.get(pk=id)
        serializer = ExpenseSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Partial Data Updated'})
        return Response(serializer.errors)


    def destroy(self,request,pk):
        id=pk
        queryset= Expense.objects.get(pk=id)
        queryset.delete()
        return Response({'message':'Data Deleted'})      