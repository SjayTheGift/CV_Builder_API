from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Resume, Experience, Education, Skill


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False) 
    class Meta:
        model = User
        fields = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=False) 
    class Meta:
        model = Experience
        fields = ('id', 'position', 'company', 'start_date', 'end_date', 'summary')


class EducationSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=False) 
    class Meta:
        model = Education
        fields = ('id', 'course', 'institution', 'duration')


class SkillSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=False) 
    class Meta:
        model = Skill
        fields = ('id', 'title')


class ResumeSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)
    class Meta:
        model = Resume
        fields = ('id','first_name', 'last_name', 'title', 'telephone', 'email', 'career_summary', 'linkedin', 'github', 'website', 'skills', 'educations', 'experiences')

    def create(self, validated_data):
        educations_data = validated_data.pop('educations')
        experiences_data = validated_data.pop('experiences')
        skills_data = validated_data.pop('skills')
        user = self.context['request'].user

        resume = Resume.objects.create(user=user, **validated_data)

        for education_data in educations_data:
            Education.objects.create(resume=resume, **education_data)

        for experience_data in experiences_data:
            Experience.objects.create(resume=resume, **experience_data)

        for skill_data in skills_data:
            Skill.objects.create(resume=resume, **skill_data)

        return resume

    
    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills')
        educations_data = validated_data.pop('educations')
        experiences_data = validated_data.pop('experiences')
        user = self.context['request'].user

        resume = Resume.objects.get(user=user)

        print(resume)

        Resume.objects.filter(id=resume.id).update(
            first_name=validated_data.get('first_name'), 
            last_name=validated_data.get('last_name'), 
            title = validated_data.get('title'), 
            telephone = validated_data.get('telephone'), 
            email = validated_data.get('email'), 
            career_summary = validated_data.get('career_summary'), 
            linkedin = validated_data.get('linkedin'),
            github = validated_data.get('github'), 
            website = validated_data.get('website'))

        for skill_item in skills_data:
            # skill_id = skill_item.get('id')
            Skill.objects.filter(resume=resume).update(**skill_item)

        
        for skill_item in skills_data:
            # skill_id = skill_item.get('id')
            Skill.objects.filter(resume=resume).update(**skill_item)

        for education_item in educations_data:
            # education_id = education_item.get('id')
            Education.objects.filter(resume=resume).update(**education_item)

        for experience_item in experiences_data:
            # experience_id = experience_item.get('id')
            Experience.objects.filter(resume=resume).update(**experience_item)

        
        return instance

