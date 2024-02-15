from django.contrib.auth.models import User
from rest_framework.serializers import CharField, ModelSerializer, ValidationError


class RetrieveUserSerializer(ModelSerializer):
    """Serializer for get user by id"""
    class Meta:
        model = User
        fields = ['username', 'email']


class UserRegisterSerializer(ModelSerializer):
    """Serializer for register users"""
    repeat_password = CharField(style={'input_type': 'password'}, write_only=True)
    email = CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'repeat_password',
        ]

    def validate(self, data):
        """Validate passwords if there match"""
        pw = data.get('password')
        pw2 = data.pop('repeat_password')
        if pw != pw2:
            raise ValidationError('Password does not match ')
        return data

    def validate_email(self, value):
        """Validate email"""
        qs = User.objects.filter(email__iexact=value)
        if qs.exists() and value == 'null':
            raise ValidationError('Email already exists')
        return value

    def validate_username(self, value):
        """Validate username"""
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise ValidationError('Username already exists')
        return value

    def create(self, validated_data):
        """Create user if data is valid"""
        user_obj = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
