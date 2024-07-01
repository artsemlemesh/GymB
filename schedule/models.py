from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    user_image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.user.username

class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    duration = models.DurationField(help_text='Duration of the class')
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    class_instance = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_participants = models.PositiveIntegerField()
    enrolled_participants = models.ManyToManyField(User, blank=True, related_name='enrolled_classes')


    def __str__(self):
        return f'{self.class_instance.name} on {self.date} from {self.start_time} to {self.end_time}'
    
    def is_full(self):
        return self.enrolled_participants.count() >= self.max_participants