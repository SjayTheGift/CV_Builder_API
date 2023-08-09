from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email',  'password', 'password2')
        extra_kwargs = {
            'password':{'write_only': True, 'required': True}
        }

    
    def create(self, validated_data):
        user = self.context["request"].user
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_query = User.objects.filter(email=user)
        data_dict = [{'email': i.email } for i in user_query]
        email = data_dict[0]['email']

        user_data = {'email': str(email)}

        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
