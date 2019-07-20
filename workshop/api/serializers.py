
from rest_framework import serializers

from registration.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            contact=validated_data['contact'],
            txn_id=validated_data['txn_id'],
            email=validated_data['email'],
            username=validated_data['username'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            college=validated_data['college'],
            branch=validated_data['branch'],
            course=validated_data['course'],
            sem=validated_data['sem'],
            address=validated_data['address'],
            pay_mode=validated_data['pay_mode'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username','password','name','email','contact','txn_id',
            'college','branch','course','sem','address','pay_mode')
