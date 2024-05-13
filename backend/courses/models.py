from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Major(models.Model):
    """ Major model """
    name = models.CharField(max_length=255)
    is_major = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        """Return string representation of the major."""   
        return f'{self.name} - {"major" if self.is_major else "core"}'
    
    def get_all_reqs(self):
        """Get all requirements associated with the major."""
        major_requirements = self.requirement.all()
        for req in major_requirements:
            print(req)
        return major_requirements


class Course(models.Model):
    """ Course model """
    id = models.TextField(primary_key=True, max_length=255)
    name = models.TextField(max_length=255)
    credit = models.IntegerField(default=4)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self) -> str:
        """Return string representation of the course."""
        return f'{self.id} - {self.name}'
    
    def get_prereqs(self):
        """Get prerequisites of the course."""
        return self.prereqs.all()

    def validate_student(self, student):
        """Validate if a student has completed prerequisites for the course."""
        prereqs = self.get_prereqs()

        for prereq_set in prereqs:
            if not student.taken_courses.filter(course__in=prereq_set.prereqs.all()).exists():
                print(prereq_set)
                return False
        return True 
    
    def get_fulfill_majors(self):
        """Get majors for which the course fulfills requirements."""
        return [req.major for req in self.major_requirements.all()]


class MajorRequirement(models.Model):
    """ Major requirement model """
    courses = models.ManyToManyField('Course', related_name='major_requirements')
    major = models.ForeignKey('Major', related_name='requirement', on_delete=models.CASCADE)
    elective = models.BooleanField(default=True)
    count = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        """Return string representation of the major requirement."""
        courses_names = " from " + ', '.join(str(course) for course in self.courses.all()) \
             if self.major.is_major and not self.elective else ""
        return f'{self.major.name} - choose {self.count}{courses_names}'


class CoursePrereq(models.Model):
    """ Course prerequisite model """
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='prereqs')
    prereqs = models.ManyToManyField('Course', related_name='required_by')

    def __str__(self):
        """Return string representation of the course prerequisite."""
        courses = ', '.join(str(course) for course in self.prereqs.all())
        return f"{self.course} requires one of [{courses}]"


# Student related classes

class StudentTakenCourse(models.Model):
    """ Student taken course model """
    student = models.ForeignKey('Student', related_name='taken_courses', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE)
    semester = models.TextField(max_length=20)


class Student(models.Model):
    """ Student model """
    class Level(models.IntegerChoices):
        NA = 0, "preschool"
        FR1 = 1, "freshman_1st"
        FR2 = 2, "freshman_2nd"
        SO1 = 3, "sophomore_1st"
        SO2 = 4, "sophomore_2nd"
        JR1 = 5, "junior_1st"
        JR2 = 6, "junior_2nd"
        SR1 = 7, "senior_1st"
        SR2 = 8, "senior_2nd"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_id = models.SmallIntegerField(choices=Level.choices, default=0)
    major = models.ManyToManyField('Major', symmetrical=False, blank=True)
    credit = models.SmallIntegerField(default=0)
    course_dict = models.JSONField(default=dict)

    def __str__(self) -> str:
        """Return string representation of the student."""
        major_str = ", ".join(m.name for m in self.major.all())
        return f"{self.user.username}, major: {major_str}, level: {self.get_level_id_display()}"
    
    def sync_courses(self):
        """Synchronize courses taken by the student."""
        current_courses = {(tc.course.id, tc.semester): tc for tc in self.taken_courses.all()}
        for semester, courses in self.course_dict.items():
            for course_data in courses:
                course_id, course_name, course_credit = course_data
                course_key = (course_id.strip(), semester)
                course, created = Course.objects.get_or_create(
                    id=course_id, defaults={'name': course_name, 'credit': course_credit, 'description': "Added from submitted histories"}
                )
                if created: print("Added new course from client submission")
                if course_key in current_courses:
                    del current_courses[course_key]
                else:
                    StudentTakenCourse.objects.create(student=self, course=course, semester=semester)
        for tc in current_courses.values():
            tc.delete()
        self.calc_taken_credit()
        self.level_id = len(self.course_dict)
        
    def calc_taken_credit(self):
        """Calculate total credits taken by the student."""
        self.credit = self.taken_courses.aggregate(total_credits=Sum('course__credit'))['total_credits'] or 0


