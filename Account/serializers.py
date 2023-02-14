from rest_framework import serializers
from django.contrib.auth import get_user_model

from Account.models import NewUser

# User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'email', 'password')

# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user





class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance