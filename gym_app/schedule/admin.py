from django.contrib import admin
from .models import Instructor, Classes, Schedule

admin.site.register(Instructor)
admin.site.register(Classes)
admin.site.register(Schedule)