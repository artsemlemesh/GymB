from rest_framework import viewsets, generics
from .models import Instructor, Classes, Schedule
from .serializers import InstructorSerializer, ClassesSerializer, ScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Schedule
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import logging


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    # permission_classes = [IsAuthenticated]


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    # permission_classes = [IsAuthenticated]



class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [IsAuthenticated]


    @action(detail=True, methods=['GET', 'POST'],  url_path='leave-class')
    def leave_class(self, request, pk=None):
        user = request.user
        schedule = self.get_object()
        if schedule.enrolled_participants.filter(id=user.id).exists():
            schedule.enrolled_participants.remove(user)
            return Response({'message': 'Successfully left the class'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not enrolled in this class'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET', 'POST'], url_path='join-class')
    def join_class(self, request, pk=None):

        user = request.user
        logging.info(f'user {user} auth: {user.is_authenticated}')
        if not user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        schedule = self.get_object()
        if not schedule.enrolled_participants.filter(id=user.id).exists():
            schedule.enrolled_participants.add(user)
            return Response({'message': 'Successfully joined the class'}, status=status.HTTP_200_OK)
        return Response({'message': 'User already enrolled in this class'}, status=status.HTTP_400_BAD_REQUEST)