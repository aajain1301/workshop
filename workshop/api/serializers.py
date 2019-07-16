from rest_framework import serializers

from registration.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','contact',
            'college_name','branch_name','sem','address')
