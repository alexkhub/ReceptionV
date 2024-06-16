from rest_framework import serializers
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'repeat_password', 'first_name', 'last_name', 'surname')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password, repeat_password = attrs.get('password', None), attrs.pop('repeat_password', None)

        if password is None or repeat_password is None:
            raise serializers.ValidationError("Вы забыли заполнить пароль")
        if password != repeat_password:
            raise serializers.ValidationError("Пароль не совпадает")

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'phone', 'surname', 'user_photo', 'slug')


class SpecialistUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_photo')


class SpecialistSerializer(serializers.ModelSerializer):
    user = SpecialistUserSerializer(read_only=True)

    class Meta:
        model = Specialist
        fields = ('id', 'user', 'position')


class List_QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_Questions
        fields = ('id', 'text')


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        advertisement = Application.objects.create(**validated_data)

        return advertisement


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
