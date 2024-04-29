from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=255)
    is_major = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {"major" if self.is_major else "core"}'
    
    def get_all_reqs(self):
        major_requirements = self.requirement.all()
        for req in major_requirements:
            print(req)
        return major_requirements

class Course(models.Model):
    course_id = models.TextField(primary_key=True, max_length=255)
    credit = models.IntegerField(default=4)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f'{self.course_id} ({self.credit})'
    
    def get_prereqs(self):
        return self.prereqs.all()

    def validate_student(self, student):
        prereqs = self.get_prereqs()

        for prereq_set in prereqs:
            if not student.taken_courses.filter(course__in=prereq_set.prereqs.all()).exists():
                print(prereq_set)
                return False
        return True 
    
    def get_fulfill_majors(self):
        # return fulfill major/core
        major_requirements = self.major_requirements.all()
        majors = set()
        for major_req in major_requirements:
            majors.add(major_req.major)
            print(f"{self.course_id} fulfills {major_req.major.name}, type: {"elective" if major_req.elective else "required"}")
        return list(majors)

class MajorRequirement(models.Model):
    courses = models.ManyToManyField('Course', related_name='major_requirements')
    major = models.ForeignKey('Major', related_name='requirement', on_delete=models.CASCADE)
    elective = models.BooleanField(default=True)
    count = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        courses_names = ', '.join(course.course_id for course in self.courses.all())
        return f'{self.major.name} - choose {self.count} - from [{courses_names}]'


class CoursePrereq(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='prereqs')
    prereqs = models.ManyToManyField('Course', related_name='required_by')

    def __str__(self):
        courses = ', '.join(course.name for course in self.prereqs.all())
        return f"{self.course.name} requires one of [{courses}]"





# Student related class


class Student(models.Model):
    class Level(models.IntegerChoices):
        FR = 1, "Freshman"
        SO = 2, "Sophomore"
        JR = 3, "Junior"
        SR = 4, "Senior"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_id = models.SmallIntegerField(choices=Level.choices)
    major = models.ManyToManyField('Major', symmetrical=False, blank=True)
    credit = models.SmallIntegerField(default=0)

    # course_dict = models.JSONField()
    # rec_cores = models.ManyToManyField('Course', related_name='core', symmetrical=False, blank=True)
    # rec_majors = models.ManyToManyField('Course', related_name='major', symmetrical=False, blank=True)

    def query_taken_courses(self):
        # return taken courses objects
        pass


    def calc_taken_credit(self):
        # update self.credit
        pass

    def generate_rec(self):
        def rec_core(self):
            # update rec cores
            pass
            
        def rec_major(self):
            # update rec majors
            pass
        pass

    def check_credit(self):
        # return True if credit >= 128 after summing up self.credit and sum(rec courses credit)
        pass

    def check_fufill_core(self):
        # return True if all core fulfilled 
        pass

    def check_fufill_major(self):
        # return True if decided major fulfilled
        pass


class Student_taken_Course(models.Model):
    student = models.ForeignKey('Student', related_name='taken_courses', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE)
    semester = models.TextField(max_length=20)



