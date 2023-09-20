from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.http import Http404

from .models import Resume, Experience, Education, Skill
from .serializers import (
    ResumeSerializer,
    ExperienceSerializer,
    EducationSerializer,
    SkillSerializer,
    )


class TestingView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()



class ResumeView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResumeSerializer
    # queryset = Resume.objects.all()

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user = valid_data['user_id']
        return Resume.objects.filter(user=user)



class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResumeSerializer
    # queryset = Resume.objects.all()
    
    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user = valid_data['user_id']
        return Resume.objects.filter(user=user)


# class ExperienceView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ExperienceSerializer

#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         resume = valid_data['resume']
#         print(resume)
#         return Experience.objects.filter(resume=resume)


# class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ExperienceSerializer

#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         # user = valid_data['user_id']
#         resume = valid_data['resume']
#         return Experience.objects.filter(resume=resume)


# class EducationView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = EducationSerializer
#     # queryset = Education.objects.all()

#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         resume = valid_data['resume']
#         print(resume)
#         return Education.objects.filter(resume=resume)



# class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = EducationSerializer
    
#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         # user = valid_data['user_id']
#         resume = valid_data['resume']
#         return Education.objects.filter(resume=resume)


# class SkillView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = SkillSerializer

#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         # user = valid_data['user_id']
#         resume = valid_data['resume']
#         return Skill.objects.filter(resume=resume)


# class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = SkillSerializer

#     def get_queryset(self):
#         token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
#         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
#         # user = valid_data['user_id']
#         resume = valid_data['resume']
#         return Skill.objects.filter(resume=resume)
