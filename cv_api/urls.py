from django.contrib import admin
from django.urls import path
from .views import (
    TestingView,
    ResumeView, 
    ResumeDetailView,
    # ExperienceView, 
    # ExperienceDetailView,
    # EducationView,
    # EducationDetailView,
    # SkillView,
    # SkillDetailView,
    )

urlpatterns = [
    path('api/cv-builder/testing/', TestingView.as_view(), name='testing'),
    path('api/cv-builder/resume/', ResumeView.as_view(), name='resume'),
    path('api/cv-builder/resume/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    # path('api/cv-builder/experience/', ExperienceView.as_view(), name='experience'),
    # path('api/cv-builder/experience/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    # path('api/cv-builder/education/', EducationView.as_view(), name='education'),
    # path('api/cv-builder/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    # path('api/cv-builder/education/', EducationView.as_view(), name='education'),
    # path('api/cv-builder/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    # path('api/cv-builder/skill/', SkillView.as_view(), name='skill'),
    # path('api/cv-builder/skill/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
]
