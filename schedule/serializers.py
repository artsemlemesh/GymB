from rest_framework import serializers

from .models import Instructor, Classes, Schedule
from django.contrib.auth.models import User


#have to define nested serializers then it can access fields from diff classes (ForeignKey, OneToOneField)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    
    class Meta:
        model = Classes
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class_instance = ClassesSerializer()
    start_time = serializers.TimeField(format="%I:%M %p")
    end_time = serializers.TimeField(format="%I:%M %p")


    class Meta:
        model = Schedule
        fields = '__all__'


