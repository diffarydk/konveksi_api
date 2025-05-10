import bleach
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        read_only_fields = ("id",)

    def validate_first_name(self, value):
        return bleach.clean(value, tags=[], strip=True)

    def validate_last_name(self, value):
        return bleach.clean(value, tags=[], strip=True)

    def validate_username(self, value):
        sanitized = bleach.clean(value, tags=[], strip=True)

        import re

        if not re.match(r"^[a-zA-Z0-9_@+.-]+$", sanitized):
            raise serializers.ValidationError(
                "Username can only contain letters, numbers, and @/./+/-/_ characters."
            )

        return sanitized


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate_username(self, value):
        # Basic sanitization for username
        return bleach.clean(value, tags=[], strip=True)

    # No need to sanitize password as it's not displayed and will be hashed

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            # Using Django's authenticate is already secure
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                return user
            else:
                # Security best practice: Use generic error messages
                # that don't reveal whether the username exists
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError(
                "Both username and password are required."
            )
