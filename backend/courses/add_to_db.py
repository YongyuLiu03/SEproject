import os, sys
sys.path.append('../../backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'se_project.settings')

import django
django.setup()
from django.conf import settings
from courses.models import Course, Major, MajorRequirement, CoursePrereq
import json
import re

# add cs required courses
cs = Major.objects.get(name="CS")
cs_elective, created = MajorRequirement.objects.get_or_create(major=cs, count=4, elective=True)


with open(os.path.join(settings.BASE_DIR, "courses/recommendor/cs_major_courses.json")) as f:
    course_lists = json.load(f)

pattern = r'^([A-Z-]+\s+\d+)\s+(.*)$'

existing_courses = Course.objects.filter(major_requirements__major=cs)

for course_list in course_lists:     
    for course_name in course_list:
        match = re.match(pattern, course_name)
        id, name = match.group(1), match.group(2)
        id = id.strip()
        name = name.strip()
        if existing_courses.filter(id=id).exists():
            # If any course in the course list already exists, skip creating a new MajorRequirement
            break
        else: 
            for course_name in course_list:
                major_requirement = MajorRequirement.objects.create(major=cs, count=1, elective=False)
                match = re.match(pattern, course_name)
                id, name = match.group(1), match.group(2)
                id = id.strip()
                name = name.strip()
                course, created = Course.objects.get_or_create(id=id, name=name)
                major_requirement.courses.add(course)

# add sh electives
with open(os.path.join(settings.BASE_DIR, "courses/recommendor/sh_elective_courses.json")) as f:
    course_lists = json.load(f)

for course_list in course_lists:   
    id, name, prereq, credit = course_list 
    id = id.strip()
    name = name.strip() 
    course, created = Course.objects.get_or_create(id=id, defaults={'name': name, 'description': prereq, 'credit': credit})
    cs_elective.courses.add(course)

# add ny electives
with open(os.path.join(settings.BASE_DIR, "courses/recommendor/ny_elective_courses.json")) as f:
    course_lists = json.load(f)

for course_list in course_lists:
    id, name, credit = course_list
    id = id.strip()
    name = name.strip() 
    course, created = Course.objects.get_or_create(id=id, defaults={'name': name, 'credit': credit})
    cs_elective.courses.add(course)


# add ny core
with open(os.path.join(settings.BASE_DIR, "courses/recommendor/ny_core_courses.json")) as f:
    course_lists = json.load(f)

course_lists["IPC/HPC/SSPC"] = course_lists["IPC"] + course_lists["HPC"] + course_lists["SSPC"]

for core_name, course_list in course_lists.items():
    if core_name in ["IPC", "HPC", "SSPC", "Language"]:
        continue
    core, created = Major.objects.get_or_create(name=core_name, is_major = False)
    count = 2 if core_name == "IPC/HPC/SSPC" else 1
    core_requirement, created = MajorRequirement.objects.get_or_create(major=core, count=count, elective=False)
    for course_info in course_list:
        id, name, credit = course_info
        id = id.strip()
        name = name.strip() 
        course, created = Course.objects.get_or_create(id=id, defaults={'name': name, 'credit': credit})
        core_requirement.courses.add(course)


# add sh core
with open(os.path.join(settings.BASE_DIR, "courses/recommendor/sh_core_courses.json")) as f:
    course_lists = json.load(f)
course_lists["IPC/HPC/SSPC"] = course_lists["IPC"] + course_lists["HPC"] + course_lists["SSPC"]

for core_name, course_list in course_lists.items():
    if core_name in ["IPC", "HPC", "SSPC", "Language"]:
        continue
    core, created = Major.objects.get_or_create(name=core_name, is_major = False)
    count = 2 if core_name == "IPC/HPC/SSPC" else 1
    core_requirement, created = MajorRequirement.objects.get_or_create(major=core, count=count, elective=False)
    for course_info in course_list:
        id, name = course_info
        id = id.strip()
        name = name.strip() 
        course, created = Course.objects.get_or_create(id=id, defaults={'name': name})
        core_requirement.courses.add(course)

# build course preqre

with open(os.path.join(settings.BASE_DIR, "courses/recommendor/sh_elective_courses.json")) as f:
    course_lists = json.load(f)

for course_list in course_lists:   
    id, name, prereq_lists, credit = course_list 
    id = id.strip()
    name = name.strip() 
    course, created = Course.objects.get_or_create(id=id)
    existed_prereqs = list(CoursePrereq.objects.filter(course=course).values_list('prereqs__id', flat=True))

    for prereq_list in prereq_lists:
        prereq_list_object = []
        prereq_list = prereq_list.split(" OR ")
        for prereq in prereq_list:
            prereq = prereq.split(" ")
            prereq_id = " ".join(prereq[:2]).strip()
            prereq_name = " ".join(prereq[2:]).strip()
            prereq_course, created = Course.objects.get_or_create(id=prereq_id, defaults={'name':prereq_name})
            prereq_list_object.append(prereq_course)
        if not CoursePrereq.objects.filter(prereqs__in=prereq_list_object, course=course).exists():
            print("adding new")
            print(prereq_list_object)
            course_prereq = CoursePrereq.objects.create(course=course)
            course_prereq.prereqs.add(*prereq_list_object)


