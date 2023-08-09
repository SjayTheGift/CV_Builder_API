from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView # new
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import Http404

from .models import Resume, Experience, Education, Skill, Achievement
from .serializers import (
    ResumeSerializer,
    ExperienceSerializer,
    EducationSerializer,
    SkillSerializer,
    AchievementSerializer,
    )


class ResumeView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ExperienceView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class EducationView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class SkillView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class AchievementView(generics.ListCreateAPIView):
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()


class AchievementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()

