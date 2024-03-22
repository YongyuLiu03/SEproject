from django.db import models

# Create your models here.

class User(models.Model):
    netid = models.TextField(primary_key=True)
    taken_courses = models.ManyToManyField(
        "self",
        related_name="taken_courses",
        related_query_name="taken_course",
        symmetrical=False
    )

class TimeSlot(models.Model):
    DAY_OF_WEEK_CHOICES = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class Course(models.Model):
    course_number_and_name = models.CharField(max_length=255, primary_key=True)
    majors = models.JSONField() 
    time = models.ManyToManyField(TimeSlot)
    prerequisites = models.ManyToManyField('self', symmetrical=False, related_name='prerequisite_for')

    def query_name(self):
        return self.course_number_and_name

    def query_major(self):
        return self.majors
    
    @staticmethod
    def filter_by_time_slot(day, start_time, end_time):
        return Course.objects.filter(
            times__day_of_week=day, 
            times__start_time__gte=start_time, 
            times__end_time__lte=end_time
        ).distinct()
    
class TakenCourse(Course):
    semester = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)

    def query_grade(self):
        return self.grade

    def query_semester(self):
        return self.semester

class CurrentSemesterCourse(Course):

    def query_prerequisite(self):
        return [course.query_name() for course in self.course.prerequisites.all()]

    def query_time_slots(self):
        return [str(timeslot) for timeslot in self.time.all()]


