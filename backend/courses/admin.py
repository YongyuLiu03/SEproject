from django.contrib import admin
from courses.models import Course, Major, Timeslot, Student

# Register your models here.
admin.site.register([Course, Major, Timeslot, Student])