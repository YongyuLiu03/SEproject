import pdb
import json
from courses.recommendor.recommendor import Recommendor
from django.conf import settings

import os, sys
sys.path.append('../../backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'se_project.settings')

import django
django.setup()


def recommend(course_history, tense=False):
    recommendor = Recommendor(course_history, identity='chinese', tense=tense)
    
    graduate_valid, recommend_courses = recommendor.recommend()

    if not graduate_valid:
        print("You cannot complete the CS major on a regular 4 courses per semester schedule, consider the overload or summer terms")
    else:
        print(recommend_courses)


if __name__ == "__main__":
    # test case 1: cs major student
    with open(os.path.join(settings.BASE_DIR, "test/course_recommend_test/test_course_history.json"), 'r') as json_file:
        course_history = json.load(json_file)
    print('+++++++++++++++++Test Case1+++++++++++++++++')
    recommend(course_history, tense=True)
    print('\n\n')
    
    # test case 2: empty course history
    course_history = {}
    print('+++++++++++++++++Test Case2+++++++++++++++++')
    recommend(course_history, tense=False)
    print('\n\n')

    # test case 3: bf major that cannot transfer to cs
    print('+++++++++++++++++Test Case3+++++++++++++++++')
    with open(os.path.join(settings.BASE_DIR, 'test/course_recommend_test/test_bf_course_history.json'), 'r') as json_file:
        course_history = json.load(json_file)
    recommend(course_history)
    print('\n\n')
