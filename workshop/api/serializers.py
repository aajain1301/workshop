
from rest_framework import serializers

from registration.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            contact=validated_data['contact'],
            college_name=validated_data['college_name'],
            branch_name=validated_data['branch_name'],
            sem=validated_data['sem'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username','password','first_name','last_name','email','contact',
            'college_name','branch_name','sem','address')

