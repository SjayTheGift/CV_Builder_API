from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Resume, Experience, Education, Skill, Achievement


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields  = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields  = "__all__"
    
        
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields  = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    # education = EducationSerializer()
    # experience = ExperienceSerializer()
    # skill = SkillSerializer()
    # achievement = AchievementSerializer()
    class Meta:
        model = Resume
        fields  = "__all__"

