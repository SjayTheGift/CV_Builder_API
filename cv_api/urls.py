from django.contrib import admin
from django.urls import path
from .views import (
    ResumeView, 
    ResumeDetailView,
    ExperienceView, 
    ExperienceDetailView,
    EducationView,
    EducationDetailView,
    SkillView,
    SkillDetailView,
    AchievementView,
    AchievementDetailView
    )

urlpatterns = [
    path('api/cv-builder/personal-info/', ResumeView.as_view(), name='personal_info'),
    path('api/cv-builder/personal-info/<int:pk>/', ResumeDetailView.as_view(), name='personal_info_detail'),
    path('api/cv-builder/experience/', ExperienceView.as_view(), name='experience'),
    path('api/cv-builder/experience/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    path('api/cv-builder/education/', EducationView.as_view(), name='education'),
    path('api/cv-builder/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    path('api/cv-builder/education/', EducationView.as_view(), name='education'),
    path('api/cv-builder/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),
    path('api/cv-builder/skill/', SkillView.as_view(), name='skill'),
    path('api/cv-builder/skill/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('api/cv-builder/achievement/', AchievementView.as_view(), name='achievement'),
    path('api/cv-builder/achievement/<int:pk>/', AchievementDetailView.as_view(), name='achievement_detail'),
]
