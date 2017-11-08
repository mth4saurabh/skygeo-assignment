from rest_framework import serializers
from api.models import User

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'registered')