from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

import random
from django.core.mail import send_mail
from .models import EmailVerificationCode

class RegionalDirectorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            'role':{'required':True},
            'region':{'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'Regional_Director':
            raise serializers.ValidationError("Only Regional Directors can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user



class CountryDirectorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region', 'country'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            "role":{"required":True},
            "region":{"required":True},
            "country":{"required":True},
            "gender":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'Country_Director':
            raise serializers.ValidationError("Only Country Directors can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user



class PFRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region', 'country', 'cluster'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            "cluster":{"required":True},
            "role":{"required":True},
            "region":{"required":True},
            "country":{"required":True},
            "gender":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'PF':
            raise serializers.ValidationError("Only PFs can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user



class PDRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region', 'country', 'project_code', 'cluster'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            "cluster":{"required":True},
            "role":{"required":True},
            "region":{"required":True},
            "country":{"required":True},
            "project_code":{"required":True},
            "gender":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'Project_director':
            raise serializers.ValidationError("Only Project Directors  can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user


class SDRRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region', 'country', 'project_code', 'cluster'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            "cluster":{"required":True},
            "role":{"required":True},
            "region":{"required":True},
            "country":{"required":True},
            "project_code":{"required":True},
            "gender":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'CDO_SDR':
            raise serializers.ValidationError("Only CDO SDRs  can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user
    


class HealthRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'gender',
            'role', 'region', 'country', 'project_code', 'cluster'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            "cluster":{"required":True},
            "role":{"required":True},
            "region":{"required":True},
            "country":{"required":True},
            "project_code":{"required":True},
            "gender":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def validate_role(self, value):
        if value != 'CDO_HEALTH':
            raise serializers.ValidationError("OnlyCDO HEALTHs  can register here.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user
    



class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']
        try:
            user = CustomUser.objects.get(email=email)
            verification = EmailVerificationCode.objects.get(user=user)
        except:
            raise serializers.ValidationError("Invalid email or code.")

        if verification.verified:
            raise serializers.ValidationError("Email already verified.")

        if verification.code != code:
            raise serializers.ValidationError("Invalid code.")

        if verification.is_expired():
            raise serializers.ValidationError("Code has expired.")

        # Mark as verified
        verification.verified = True
        verification.save()
        return attrs
