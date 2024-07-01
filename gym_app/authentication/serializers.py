
from rest_framework import serializers

from django.contrib.auth.models import User


#have to define nested serializers then it can access fields from diff classes (ForeignKey, OneToOneField)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'