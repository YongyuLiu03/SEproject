from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    class Level(models.IntegerChoices):
        FR = 1, "Freshman"
        SO = 2, "Sophomore"
        JR = 3, "Junior"
        SR = 4, "Senior"
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    # net_id = models.TextField(primary_key=True, max_length=10)
    # name = models.TextField(max_length=50)
    level_id = models.SmallIntegerField(choices=Level.choices)
    major = models.ManyToManyField('Major', symmetrical=False, blank=True)
    credit = models.SmallIntegerField()


class Course(models.Model):
    course_id = models.TextField(primary_key=True, max_length=20)
    name = models.TextField(max_length=50)
    credit = models.IntegerField()
    description = models.TextField(max_length=255, blank=True)
    prereqs = models.ManyToManyField('Course', symmetrical=False, related_name='pre_req_of', blank=True)
    times = models.ManyToManyField('Timeslot', related_name='courses', blank=True)
    majors = models.ManyToManyField('Major', related_name="courses", blank=True)
    at_fall = models.BooleanField(default=True)
    at_spring = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.course_id} {self.name}'

class Student_taken_Course(models.Model):
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.TextField(max_length=20)
    # grade = models.TextField(max_length=2, blank=True)

class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.TextField()
    is_major = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

class Timeslot(models.Model):
    class Day(models.IntegerChoices):
        MON = 1, "Monday"
        TUE = 2, "Tuesday"
        WED = 3, "Wednesday"
        THU = 4, "Thursday"
        FRI = 5, "Friday"
        SAT = 6, "Saturday"
        SUN = 7, "Sunday"

    timeslot_id = models.AutoField(primary_key=True)
    day_of_week = models.PositiveSmallIntegerField(choices=Day.choices)
    begin_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)



#     def query_name(self):
#         return self.course_number_and_name

#     def query_major(self):
#         return self.majors
    
#     @staticmethod
#     def filter_by_time_slot(day, start_time, end_time):
#         return Course.objects.filter(
#             times__day_of_week=day, 
#             times__start_time__gte=start_time, 
#             times__end_time__lte=end_time
#         ).distinct()

# class TakenCourse(Course):
#     semester = models.CharField(max_length=20)
#     grade = models.CharField(max_length=2)
#     users = models.ManyToManyField(User, through='UserCourse', related_name='taken_courses')
    
#     def query_grade(self):
#         return self.grade

#     def query_semester(self):
#         return self.semester
    

