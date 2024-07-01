from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, ClassesViewSet, ScheduleViewSet



router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'schedule', ScheduleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
