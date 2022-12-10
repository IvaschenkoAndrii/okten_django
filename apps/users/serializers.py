from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from apps.users.models import UserModel as User

from ..auto_park.serializers import AutoParkSerializer

UserModel: Type[User] = get_user_model()

from django.db import transaction

from core.services.email_service import EmailService

from .models import ProfileModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('name', 'surname', 'age', 'phone')


class UserSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = UserModel

        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at',
            'last_login', 'profile', 'auto_parks'
        )

        read_only_field = ('id', 'is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at', 'last_login')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register_email(user)
        return user


class UserSerializerMakeActive(ModelSerializer):
    class Meta:
        model = UserModel

        fields = (
            'id', 'is_active'
        )


class UserSerializerMakeAdmin(ModelSerializer):
    class Meta:
        model = UserModel

        fields = (
            'id', 'is_staff'
        )


class AvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
