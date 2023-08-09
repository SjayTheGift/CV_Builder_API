from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializers import (LogInSerializer, UserSerializer)



User = get_user_model()


class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
